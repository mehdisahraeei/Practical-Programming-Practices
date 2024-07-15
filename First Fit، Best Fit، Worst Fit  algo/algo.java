public class MemoryAllocation {

    // First Fit Algorithm
    public static int[] firstFit(int[] blocks, int[] processes) {
        int[] allocation = new int[processes.length];
        for (int i = 0; i < processes.length; i++) {
            allocation[i] = -1;
            for (int j = 0; j < blocks.length; j++) {
                if (blocks[j] >= processes[i]) {
                    allocation[i] = j;
                    blocks[j] -= processes[i];
                    break;
                }
            }
        }
        return allocation;
    }

    // Best Fit Algorithm
    public static int[] bestFit(int[] blocks, int[] processes) {
        int[] allocation = new int[processes.length];
        for (int i = 0; i < processes.length; i++) {
            allocation[i] = -1;
            int bestIdx = -1;
            for (int j = 0; j < blocks.length; j++) {
                if (blocks[j] >= processes[i]) {
                    if (bestIdx == -1 || blocks[j] < blocks[bestIdx]) {
                        bestIdx = j;
                    }
                }
            }
            if (bestIdx != -1) {
                allocation[i] = bestIdx;
                blocks[bestIdx] -= processes[i];
            }
        }
        return allocation;
    }

    // Worst Fit Algorithm
    public static int[] worstFit(int[] blocks, int[] processes) {
        int[] allocation = new int[processes.length];
        for (int i = 0; i < processes.length; i++) {
            allocation[i] = -1;
            int worstIdx = -1;
            for (int j = 0; j < blocks.length; j++) {
                if (blocks[j] >= processes[i]) {
                    if (worstIdx == -1 || blocks[j] > blocks[worstIdx]) {
                        worstIdx = j;
                    }
                }
            }
            if (worstIdx != -1) {
                allocation[i] = worstIdx;
                blocks[worstIdx] -= processes[i];
            }
        }
        return allocation;
    }

    public static void main(String[] args) {
        int[] blocks = {20, 10, 30};
        int[] processes = {15, 10, 25};

        int[] firstFitAllocation = firstFit(blocks.clone(), processes);
        System.out.println("First Fit Allocation: " + Arrays.toString(firstFitAllocation));

        int[] bestFitAllocation = bestFit(blocks.clone(), processes);
        System.out.println("Best Fit Allocation: " + Arrays.toString(bestFitAllocation));

        int[] worstFitAllocation = worstFit(blocks.clone(), processes);
        System.out.println("Worst Fit Allocation: " + Arrays.toString(worstFitAllocation));
    }
}

