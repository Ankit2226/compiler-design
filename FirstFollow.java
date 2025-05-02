import java.util.*;

public class FirstFollow {

    static Map<String, List<String>> grammar = new HashMap<>();
    static Map<String, Set<String>> first = new HashMap<>();
    static Map<String, Set<String>> follow = new HashMap<>();
    static Set<String> nonTerminals = new HashSet<>();
    static Set<String> terminals = new HashSet<>();

    public static void main(String[] args) {
        // Define grammar using "EPS" instead of ε
        grammar.put("E", Arrays.asList("T E'"));
        grammar.put("E'", Arrays.asList("+ T E'", "EPS"));
        grammar.put("T", Arrays.asList("F T'"));
        grammar.put("T'", Arrays.asList("* F T'", "EPS"));
        grammar.put("F", Arrays.asList("( E )", "id"));

        // Initialize FIRST and FOLLOW sets
        for (String nt : grammar.keySet()) {
            nonTerminals.add(nt);
            first.put(nt, new HashSet<>());
            follow.put(nt, new HashSet<>());
        }

        // Identify terminals
        for (List<String> productions : grammar.values()) {
            for (String prod : productions) {
                String[] symbols = prod.split(" ");
                for (String sym : symbols) {
                    if (!grammar.containsKey(sym) && !sym.equals("EPS")) {
                        terminals.add(sym);
                    }
                }
            }
        }

        // Compute FIRST sets
        for (String nt : grammar.keySet()) {
            computeFirst(nt);
        }

        // Start symbol FOLLOW contains $
        String startSymbol = "E";
        follow.get(startSymbol).add("$");

        // Compute FOLLOW sets
        boolean changed;
        do {
            changed = false;
            for (String nt : grammar.keySet()) {
                for (String prod : grammar.get(nt)) {
                    String[] symbols = prod.split(" ");
                    for (int i = 0; i < symbols.length; i++) {
                        String B = symbols[i];
                        if (nonTerminals.contains(B)) {
                            Set<String> followB = follow.get(B);
                            int beforeSize = followB.size();

                            // Case 1: symbols after B
                            boolean allNullable = true;
                            for (int j = i + 1; j < symbols.length; j++) {
                                Set<String> firstNext = computeFirst(symbols[j]);
                                followB.addAll(removeEPS(firstNext));
                                if (!firstNext.contains("EPS")) {
                                    allNullable = false;
                                    break;
                                }
                            }

                            // Case 2: B is at end or all after can be EPS
                            if (i == symbols.length - 1 || allNullable) {
                                followB.addAll(follow.get(nt));
                            }

                            if (followB.size() > beforeSize) {
                                changed = true;
                            }
                        }
                    }
                }
            }
        } while (changed);

        // Print FIRST sets
        System.out.println("FIRST sets:");
        for (String nt : grammar.keySet()) {
            System.out.println("FIRST(" + nt + ") = " + sortedSet(first.get(nt)));
        }

        // Print FOLLOW sets
        System.out.println("\nFOLLOW sets:");
        for (String nt : grammar.keySet()) {
            System.out.println("FOLLOW(" + nt + ") = " + sortedSet(follow.get(nt)));
        }
    }

    static Set<String> computeFirst(String symbol) {
        if (!nonTerminals.contains(symbol)) {
            return new HashSet<>(Collections.singletonList(symbol));
        }

        if (!first.get(symbol).isEmpty()) {
            return first.get(symbol);
        }

        for (String production : grammar.get(symbol)) {
            String[] symbols = production.split(" ");
            boolean allNullable = true;

            for (String sym : symbols) {
                Set<String> symFirst = computeFirst(sym);
                first.get(symbol).addAll(removeEPS(symFirst));
                if (!symFirst.contains("EPS")) {
                    allNullable = false;
                    break;
                }
            }

            if (allNullable) {
                first.get(symbol).add("EPS");
            }
        }

        return first.get(symbol);
    }

    static Set<String> removeEPS(Set<String> set) {
        Set<String> result = new HashSet<>(set);
        result.remove("EPS");
        return result;
    }

    static List<String> sortedSet(Set<String> set) {
        List<String> list = new ArrayList<>(set);
        Collections.sort(list);
        return list;
    }
}