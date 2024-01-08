public class Power {
    public static void main(String args[]) {
        System.out.println(POW(6, 8));
    }

    static public int POW(int a, int b){
        int result = 1;
        for(int i = 0; i < b; i++)
            result *= a;
        return result;
        }
}
