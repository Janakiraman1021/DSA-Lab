class InsertionSort {
    public static void ins(int arr[]) {
        int n = arr.length;
        for (int j = 1; j < n; j++) {
            int key = arr[j];
            int i = j - 1;
            while ((i > -1) && (arr[i] > key)) {
                arr[i + 1] = arr[i];
                i--;
            }
            arr[i + 1] = key;
        }
    }

    public static void main(String a[]) {
        int a1[] = {9, 14, 3, 2, 43, 11, 58, 22};
        System.out.println("Before Insertion Sort: ");
        for (int i : a1) {
            System.out.print(i + " ");
        }
        System.out.println();
        ins(a1);
        System.out.println("After Insertion Sort: ");
        for (int i : a1) {
            System.out.print(i + " ");
        }
    }
}
