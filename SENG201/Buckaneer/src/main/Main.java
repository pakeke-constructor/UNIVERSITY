package main;


import javax.swing.JFrame;
import javax.swing.JLabel;


/**
 * The starting class that runs the program.
 * All this class does is run a main method that
 * instantiates a GameLogic instance and adds some basic settings.
 * 
 */
public class Main {
	private  static GameLogic logic = new GameLogic();	
	
	public static void main(String[] args) {
		/**
		 * This method is called when the program initially runs.
		 * 
		 * 
		 * @param args Unused.
		 * 
		 */
		JFrame window = new JFrame();
		window.setBounds(100, 100, 1280, 720);
		window.setTitle("Buckaneer");;
		window.setResizable(false);
		window.add(logic);
		window.setVisible(true);
		window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}
}
