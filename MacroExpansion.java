import java.io.*;
import java.util.*;

public class MacroExpansion {
    public static void main(String[] args) {
        String macroFile = "macro.txt";       
        String assemblyFile = "assembly.txt"; 

        
        Map<String, Macro> macroMap = loadMacros(macroFile);

        String expandedCode = processAssembly(assemblyFile, macroMap);

        
        System.out.println("\nExpanded Assembly Code:");
        System.out.println(expandedCode);
    }

    static class Macro {
        String name;
        List<String> parameters;
        List<String> body;

        Macro(String name, List<String> parameters, List<String> body) {
            this.name = name;
            this.parameters = parameters;
            this.body = body;
        }

        String expand(List<String> arguments) {
            if (arguments.size() != parameters.size()) {
                return "ERROR: Incorrect number of arguments for " + name + "\n";
            }
            StringBuilder expanded = new StringBuilder();
            for (String line : body) {
                String expandedLine = line;
                for (int i = 0; i < parameters.size(); i++) {
                    expandedLine = expandedLine.replace(parameters.get(i), arguments.get(i));
                }
                expanded.append("+" + expandedLine).append("\n"); 
            }
            return expanded.toString();
        }
    }

    private static Map<String, Macro> loadMacros(String filename) {
        Map<String, Macro> macroMap = new HashMap<>();
        try (BufferedReader br = new BufferedReader(new FileReader(filename))) {
            String line;
            while ((line = br.readLine()) != null) {
                if (line.startsWith("MACRO")) {
                    String macroHeader = br.readLine().trim(); 
                    String[] headerParts = macroHeader.split("[ ,]+"); 
                    String macroName = headerParts[0];
                    List<String> parameters = Arrays.asList(Arrays.copyOfRange(headerParts, 1, headerParts.length));

                    
                    List<String> body = new ArrayList<>();
                    while ((line = br.readLine()) != null && !line.equals("MEND")) {
                        body.add(line);
                    }
  
                    macroMap.put(macroName, new Macro(macroName, parameters, body));
                }
            }
        } catch (IOException e) {
            System.err.println("Error reading macro file: " + e.getMessage());
        }
        return macroMap;
    }

    private static String processAssembly(String filename, Map<String, Macro> macroMap) {
        StringBuilder expandedCode = new StringBuilder();
        try (BufferedReader br = new BufferedReader(new FileReader(filename))) {
            String line;
            while ((line = br.readLine()) != null) {
                line = line.trim();
                if (line.isEmpty()) continue; 
                
                String[] parts = line.split("[ ,]+"); 
                String instruction = parts[0];
 
                if (macroMap.containsKey(instruction)) {
                    List<String> arguments = Arrays.asList(Arrays.copyOfRange(parts, 1, parts.length));
                    expandedCode.append(macroMap.get(instruction).expand(arguments));
                } else {
                    expandedCode.append(line).append("\n"); 
                }
            }
        } catch (IOException e) {
            System.err.println("Error reading assembly file: " + e.getMessage());
        }
        return expandedCode.toString();
    }
}
