package main;

/**
 * 
 * KeyboardHandler is the class responsible for text input when typing out the name for the ship
 * 
 *
 */
public class KeyboardHandler {
	private static String shipName = "";
	private static char[] validChars = new char[] {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' '};
	
	
	/**
	 * returns if the name of the ship is valid
	 * @return whether name of ship is valid
	 */
	public static boolean validName() {
		return (shipName.length() >= 3);
 	}
	
	
	/**
	 * handles the input from the user and turns it into part of the ship name if it meets the required criteria
	 * 
	 * @param cChar character to add onto ship name
	 */
	public static void handleInput(char cChar) {
		if(charIsValid(cChar) && shipName.length() < 15) {
			if(cChar == ' ') {
				if (!shipName.endsWith(" ")) {
					shipName += String.valueOf(cChar);
				}
			}else {
				shipName += String.valueOf(cChar);
			}
		}else if(cChar == '\b') {
			//remove last character from string
			shipName = shipName.substring(0, Math.max(0, shipName.length() - 1));
		}
	}
	
	
	/**
	 * sees if input is valid
	 * @param cChar the character to check
	 */
	public static boolean charIsValid(char cChar) {
		for(int i=0; i < validChars.length; i++) {
			if(cChar == validChars[i]) {
				return true;
			}
		}
		return false;
	}
	
	public static String getShipName() {
		return shipName;
	}
}
