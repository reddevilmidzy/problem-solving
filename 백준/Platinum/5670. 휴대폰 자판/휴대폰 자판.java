import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder stringBuilder = new StringBuilder();

        String value = bufferedReader.readLine();
        int n;

        while (value != null) {
            n = Integer.parseInt(value);
            Trie trie = new Trie();
            List<String> words = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                String tmp = bufferedReader.readLine();
                trie.insert(tmp);
                words.add(tmp);
            }

            int typeCount = 0;

            for (String word : words) {
                int tmp = 1;
                for (int i = 1; i < word.length(); i++) {
                    int count = trie.count(word.substring(0, i));
                    if (count > 1) {
                        tmp++;
                    }
                }
                typeCount += tmp;
            }
            stringBuilder.append(String.format("%.2f\n", (double) typeCount / n));
            value = bufferedReader.readLine();
        }

        System.out.print(stringBuilder);
    }

    static class Node {
        Map<Character, Node> children = new HashMap<>();
        int endOfWord = 0;

        @Override
        public String toString() {
            return children.toString();
        }
    }

    static class Trie {
        Node rootNode = new Node();

        void insert(String str) {
            Node node = this.rootNode;

            for (int i = 0; i < str.length(); i++) {
                node = node.children.computeIfAbsent(str.charAt(i), key -> new Node());
            }
            node.endOfWord = 1;
        }

        int count(String str) {
            Node node = this.rootNode;

            for (int i = 0; i < str.length(); i++) {
                node = node.children.getOrDefault(str.charAt(i), null);
                if (node == null) {
                    return 0;
                }
            }
            return node.children.values().size() + node.endOfWord;
        }

        @Override
        public String toString() {
            return rootNode.toString();
        }
    }
}
