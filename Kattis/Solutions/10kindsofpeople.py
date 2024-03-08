import java.io.*;
import java.util.StringTokenizer;
import java.util.ArrayDeque;

public class Main {
    static class Node {
        int x, y, terr, group;

        public Node(int x, int y, int terr, int group) {
            this.x = x;
            this.y = y;
            this.terr = terr;
            this.group = group;
        }
    }

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int r = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());
        Node[][] board = new Node[r][c];
        for (int i = 0; i < r; i++) {
            String input = br.readLine();
            for (int j = 0; j < c; j++) {
                board[i][j] = new Node(i, j, input.charAt(j) - '0', 0);
            }
        }
        BFS(board);
        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int rl = Integer.parseInt(st.nextToken()) - 1;
            int cl = Integer.parseInt(st.nextToken()) - 1;
            int r2 = Integer.parseInt(st.nextToken()) - 1;
            int c2 = Integer.parseInt(st.nextToken()) - 1;
            if (board[rl][cl].group == board[r2][c2].group) {
                if (board[rl][cl].terr == 1)
                    System.out.println("decimal");
                else
                    System.out.println("binary");
            } else {
                System.out.println("neither");
            }
        }
    }

    private static void BFS(Node[][] board) {
        int gc = 1;
        int visited = 0;
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[i].length; j++) {
                if (board[i][j].group == 0) {
                    ArrayDeque<Node> ar = new ArrayDeque<>();
                    board[i][j].group = gc;
                    ar.add(board[i][j]);
                    while (!ar.isEmpty()) {
                        Node temp = ar.removeFirst();
                        try {
                            Node to = board[temp.x][temp.y + 1];
                            if (temp.y + 1 < board[0].length && board[temp.x][temp.y + 1].group == 0
                                    && board[temp.x][temp.y + 1].terr == temp.terr) {
                                board[temp.x][temp.y + 1].group = gc;
                                ar.add(board[temp.x][temp.y + 1]);
                                visited++;
                            }
                        } catch (ArrayIndexOutOfBoundsException ex) {
                        }
                        try {
                            Node to = board[temp.x][temp.y - 1];
                            if (temp.y - 1 >= 0 && board[temp.x][temp.y - 1].group == 0
                                    && board[temp.x][temp.y - 1].terr == temp.terr) {
                                board[temp.x][temp.y - 1].group = gc;
                                ar.add(board[temp.x][temp.y - 1]);
                                visited++;
                            }
                        } catch (ArrayIndexOutOfBoundsException ex) {
                        }
                        try {
                            Node to = board[temp.x + 1][temp.y];
                            if (temp.x + 1 < board.length && board[temp.x + 1][temp.y].group == 0
                                    && board[temp.x + 1][temp.y].terr == temp.terr) {
                                board[temp.x + 1][temp.y].group = gc;
                                ar.add(board[temp.x + 1][temp.y]);
                                visited++;
                            }
                        } catch (ArrayIndexOutOfBoundsException ex) {
                        }
                        try {
                            Node to = board[temp.x - 1][temp.y];
                            if (temp.x - 1 >= 0 && board[temp.x - 1][temp.y].group == 0
                                    && board[temp.x - 1][temp.y].terr == temp.terr) {
                                board[temp.x - 1][temp.y].group = gc;
                                ar.add(board[temp.x - 1][temp.y]);
                                visited++;
                            }
                        } catch (ArrayIndexOutOfBoundsException ex) {
                        }
                    }
                    gc++;
                }
            }
        }
    }
}
