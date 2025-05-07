import java.util.Scanner;

public class imc {
    public static void main(String[] args) {
        Scanner leitura = new Scanner(System.in);

        System.out.print("Digite seu peso em kg: ");
        double peso = leitura.nextDouble();

        System.out.print("Digite sua sua altura (ex.: 1,75): ");
        double altura = leitura.nextDouble();

        double imc = peso / (altura * altura);
        System.out.printf("Seu IMC é de %.2f.", imc);
        leitura.close();
    }
}