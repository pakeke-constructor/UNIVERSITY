package main;

import java.awt.event.KeyEvent;
import java.util.Random;


public class EventHandler {
	
	private Random random = new Random();
	private int numberPressed;
	
	
	public void generateRandomEvent(int chance) {
		/*
		Generates and calls a random event depending on param chance.
		chance = 2: pirates or no event.
		chance = 3: weather, pirates, or no event.
		chance = 4: weather, pirates, abandoned ship, or no event.

		@param chance Denotes what events can happen. (See main method docs)

		*/
		int randEvent = random.nextInt(chance);
		if (randEvent == 1) {
			pirateEvent();
		}else if (randEvent == 2) {
			weatherEvent();
		}else if (randEvent == 3) {
			abandonedShipEvent();
		}
	}
	
	
	public void pirateEvent() {
		/*
		Invokes a pirate event and shows a pop-up to user.

		The higher the player's fighting chance, (better items,) the more likely
		the player is to get away for free. Otherwise, the pirates will take
		$1000 of your ship stock and leave. 
		If the player does not have $1000 worth of stock, gameState will be
		set to GAMEOVER.
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
	
	
	public void weatherEvent() {
		/*
		Weather event damages hull by a random amount, and shows pop-up
		*/
		GameLogic.setPaused(true);
		GameLogic.setEventImage(GameData.getWeatherEventMessage());
		Ship.changeHull(-random.nextInt(30));
		endEvent();
	}
	
	public void abandonedShipEvent() {
		/*
		Abandoned ship event gives player money and shows pop-up
		*/
		GameLogic.setPaused(true);
		GameLogic.setEventImage(GameData.getAbandonedShipMessage());
		Ship.changeMoney(random.nextInt(500));
		endEvent();
	}
	
	public void endEvent() {
		/*
		Blocks the game loop until player hits spacebar.
		After player hits the spacebar, 

		*/
		while(GameLogic.getCurrentChar() != KeyEvent.VK_SPACE) {
			System.out.println(GameLogic.getCurrentChar());
		}
		GameLogic.setCurrentChar(KeyEvent.CHAR_UNDEFINED);
		GameLogic.setEventImage(GameData.getEmpty());
		GameLogic.setPaused(false);
	}
	
	public boolean validKey(char cChar) {
		/*
		Takes a character key as a param, and mutates the .numberPressed
		field appropriately.

		@param cChar the key that was pressed

		@return whether the key was recognized or not
		*/

		//System.out.println("sticu");
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
