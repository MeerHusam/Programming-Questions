import java.util.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine());

        // This set contains names of all people who have been involved in the rumor.
        Set<String> people = new HashSet<>();

        // This set contains names of people who have heard the rumor from someone else.
        Set<String> heardFrom = new HashSet<>();

        // This list stores relationships of type "p1 ?? p2".
        List<String[]> unknownRelations = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            String[] parts = sc.nextLine().split(" ");
            String p1 = parts[0];
            String relation = parts[1];
            String p2 = parts[2];

            // Populate the people set.
            people.add(p1);
            people.add(p2);

            if ("->".equals(relation)) {
                // p2 heard from p1.
                heardFrom.add(p2);
            } else {
                // Store the unknown relation for further analysis.
                unknownRelations.add(new String[] { p1, p2 });
            }
        }

        // Repeatedly go through the unknown relations until no more people can be
        // identified as having heard from someone.
        boolean changed;
        do {
            changed = false;
            Iterator<String[]> iterator = unknownRelations.iterator();
            while (iterator.hasNext()) {
                String[] relation = iterator.next();
                String p1 = relation[0];
                String p2 = relation[1];

                // If p1 is a known listener, then p2 also becomes a listener and vice versa.
                if (heardFrom.contains(p1) && !heardFrom.contains(p2)) {
                    heardFrom.add(p2);
                    iterator.remove();
                    changed = true;
                } else if (heardFrom.contains(p2) && !heardFrom.contains(p1)) {
                    heardFrom.add(p1);
                    iterator.remove();
                    changed = true;
                }
            }
        } while (changed);

        // Those who haven't heard from anyone are the potential sources.
        people.removeAll(heardFrom);

        // Sort the names alphabetically.
        List<String> result = new ArrayList<>(people);
        Collections.sort(result);

        // Print the result.
        for (String name : result) {
            System.out.println(name);
        }
    }
}
