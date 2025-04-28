public class Factorial {
    private int numero;

    public Factorial(int numero) {
        this.numero = numero;
    }

    public int calcular() {
        int resultado = 1;
        for (int i = 2; i <= numero; i++) {
            resultado *= i;
        }
        return resultado;
    }

    public static void main(String[] args) {
        Factorial f = new Factorial(5);
        System.out.println(f.calcular()); // Salida: 120
    }
}