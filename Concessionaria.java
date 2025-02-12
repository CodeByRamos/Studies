package joao_ramos;
import javax.swing.JOptionPane;
public class Concessionaria {
	public static void main (String args []) {
		
		Automovel e = new Automovel();
		
		String mr,md,cr,pr,an;
		double pc;
		
		mr = JOptionPane.showInputDialog("digite a marca:");
		md = JOptionPane.showInputDialog("digite o modelo:");
		cr = JOptionPane.showInputDialog("digite a cor:");
		pr = JOptionPane.showInputDialog("digite o preço:");
		an = JOptionPane.showInputDialog("digite o ano");
		
		pc = Double.parseDouble(pr);
		
		e.marca = mr;
		e.modelo = md;
		e.cor = cr;
		e.preço = pc;
		e.ano = an;
		
		e.Informa_automovel();
	}

}
