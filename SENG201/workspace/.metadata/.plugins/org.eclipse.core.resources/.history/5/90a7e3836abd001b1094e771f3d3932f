package main;

import java.awt.event.KeyEvent;
import java.util.Random;


public class EventHandler {
	
	private Random random = new Random();
	private int numberPressed;
	
	/*
	 * Generates and calls a random event depending on parameter chance.
	 * chance = 2: pirates or no event.
	 * chance = 3: weather, pirates, or no event.
	 * chance = 4: weather, pirates, abandoned ship, or no event.
	 * 
	 * @param chance Denotes what events can happen. (See main method documentations)
	*/
	public void generateRandomEvent(int chance) {
		int randEvent = random.nextInt(chance);
		if (randEvent == 1) {
			pirateEvent();
		}else if (randEvent == 2) {
			weatherEvent();
		}else if (randEvent == 3) {
			abandonedShipEvent();
		}
	}
	
	/*
	 * 	Invokes a pirate event and shows a pop-up to user.
	 *  The higher the player's fighting chance, (better items,) the more likely
	 *  the player is to get away for free. Otherwise, the pirates will take
	 *  $1000 of your ship stock and leave. 
	 *  If the player does not have $1000 worth of stock, gameState will be
	 *  set to GAMEOVER.
	 */
	public void pirateEvent() {
		/*
		*/
		GameLogic.setPaused(true);
		GameLogic.setEventImage(GameData.getPirateEventMessage1());
		int randSuccess = random.nextInt(5);
		boolean keyValid = false;
		while(!keyValid) {
			keyValid = validKey(GameLogic.getCurrentChar());
		}
		if (random.nextInt(Ship.getFightingChance()) == 0) {
			GameLogic.setEventImage(GameData.getPirateEventMessage3());
		}else if (numberPressed == (randSuccess + 1)){
			GameLogic.setEventImage(GameData.getPirateEventMessage3());
		}else {
			if (Ship.inventoryWorth() >= 1000) {
				Ship.setInventory(new int[7]);
				GameLogic.setEventImage(GameData.getPirateEventMessage2());
			}else {
				GameLogic.setEventImage(GameData.getPirateEventMessage2());
				endEvent();
				GameLogic.state = State.GAMEOVER;
				GameLogic.setGameOverImage(GameData.getGameOverPirates());
			}
			
		}
		endEvent();
	}
	
	/*
	 * 	Weather event damages hull by a random amount, and shows pop-up 	
	 */
	public void weatherEvent() {
		GameLogic.setPaused(true);
		GameLogic.setEventImage(GameData.getWeatherEventMessage());
		Ship.changeHull(-random.nextInt(30));
		endEvent();
	}
	
	/*
	 * Abandoned ship event gives player money and shows pop-up
	 */
	public void abandonedShipEvent() {
		GameLogic.setPaused(true);
		GameLogic.setEventImage(GameData.getAbandonedShipMessage());
		Ship.changeMoney(random.nextInt(500));
		endEvent();
	}
	
	/*
	 * 	Blocks the game loop until player hits space bar.
	 * After player hits the space bar, game loop resumes.
	 */
	public void endEvent() {
		while(GameLogic.getCurrentChar() != KeyEvent.VK_SPACE) {
			//System.out.println(GameLogic.getCurrentChar());
			// block event queue
		}
		GameLogic.setCurrentChar(KeyEvent.CHAR_UNDEFINED);
		GameLogic.setEventImage(GameData.getEmpty());
		GameLogic.setPaused(false);
	}
	
	/*
	 * 	Blocks the game loop until player hits key denoted by key tag.
	 * After player hits the specified key, game loop resumes.
	 */
	public void endEvent(int[] validKeys) {
		boolean isKeyValid = false;
		for(int i=0; i<validKeys.length; i++) {
			if(GameLogic.getCurrentChar() == validKeys[i]) {
				isKeyValid = true;
			}
		}
		while(!isKeyValid) {
			for(int i=0; i<validKeys.length; i++) {
				if(GameLogic.getCurrentChar() == validKeys[i]) {
					isKeyValid = true;
				}
			}
			// block event queue
		}
		GameLogic.setCurrentChar(KeyEvent.CHAR_UNDEFINED);
		GameLogic.setEventImage(GameData.getEmpty());
		GameLogic.setPaused(false);		
	}

	/*
	 * 	Takes a character key as a parameter, and mutates the .numberPressed
	 *  field appropriately.
	 *  
	 *  @param cChar the key that was pressed
	 *  
	 *  @return whether the key was recognized or not 
	*/
	public boolean validKey(char cChar) {
		if (cChar == KeyEvent.VK_1) {
			numberPressed = 1;
			return true;
		}else if (cChar == KeyEvent.VK_2) {
			numberPressed = 2;
			return true;
		}else if (cChar == KeyEvent.VK_3) {
			numberPressed = 3;
			return true;
		}else if (cChar == KeyEvent.VK_4) {
			numberPressed = 4;
			return true;
		}else if(cChar == KeyEvent.VK_5) {
			numberPressed = 5;
			return true;
		}else if (cChar == KeyEvent.VK_6) {
			numberPressed = 6;
			return true;
		}
		return false;
	}
}
