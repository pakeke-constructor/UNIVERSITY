package main;

import java.awt.Image;
import java.awt.Toolkit;
import java.util.HashMap;
import java.util.Set;

import org.junit.Test;

import static org.junit.Assert.fail;

/**
 * Class that holds all the internal game information that is unrelated
 * to the main game state machine.
 * E.g: Images and price of items and created and generated here.
 */
public class GameData {
	private static Toolkit t = Toolkit.getDefaultToolkit();
	private static Image path01 = t.getImage("images/paths/path01.png");
	private static Image path02 = t.getImage("images/paths/path02.png");
	private static Image path03 = t.getImage("images/paths/path03.png");
	private static Image path04 = t.getImage("images/paths/path04.png");
	private static Image path12 = t.getImage("images/paths/path12.png");
	private static Image path13 = t.getImage("images/paths/path13.png");
	private static Image path14 = t.getImage("images/paths/path14.png");
	private static Image path23 = t.getImage("images/paths/path23.png");
	private static Image path24 = t.getImage("images/paths/path24.png");
	private static Image path34 = t.getImage("images/paths/path34.png");
	
	// hashMap that points to all path drawing objects, i.e. path34, path12, etc.
	private static HashMap<String, Image> paths = new HashMap<String, Image>();
	private static Image empty = t.getImage("images/empty.png");
	private Button islandButton0 = new Button(10, 150, 370, 500);
	private Button islandButton1 = new Button(440, 570, 290, 370);
	private Button islandButton2 = new Button(330, 580, 500, 640);
	private Button islandButton3 = new Button(750, 872, 290, 350);
	private Button islandButton4 = new Button(732, 891, 444, 514);
	private static Image pirateEventMessage1 = t.getImage("images/piratemessage.jpg");
	private static Image pirateEventMessage2 = t.getImage("images/piratemessage2.jpg");
	private static Image pirateEventMessage3 = t.getImage("images/piratemessage3.jpg");
	private static Image weatherEventMessage = t.getImage("images/badweather.jpg");
	private static Image abandonedShipMessage = t.getImage("images/abandondedship.jpg");
	private static Image noMoneyMessage = t.getImage("images/nomoney.jpg");
	private static Image noSpaceMessage = t.getImage("images/bootytoobig.jpg");
	private static Image noItemsMessage = t.getImage("images/noitems.jpg");
	private static Image repairError = t.getImage("images/repairerror.jpg");
	private static Image shopButton = t.getImage("images/shopbutton.jpg");
	private static Image inventoryButton = t.getImage("images/inventory.jpg");
	private static Image priceInfoButton = t.getImage("images/priceinfobutton.jpg");
	private static Image gameOverMoney = t.getImage("images/gameovernomoney.png");
	private static Image gameOverPirates = t.getImage("images/gameoverpirates.png");
	private static Image gameOverGood = t.getImage("images/gameovergood.png");
	private static Image gameOverHull = t.getImage("images/gameoverhull.png");
	private static int[][] sellingData;
	private static int[][] buyingData;
	
	static {
		// initialize hashMap of path images
		for (int i=0; i<5; i++) {
			for (int j=0; j<5; j++) {
				String key1 = ("path" + i) + j;
				String key2 = ("path" + j) + i;
				if ((i != j) && (!paths.containsKey(key1)) && (!paths.containsKey(key2))) {
					Image image = t.getImage(("images/paths/path" + i) + j + ".png");
					paths.put(key1, image);
					paths.put(key2, image);
				}
			}
		}
	}
	
	/**
	 * This static method returns the path image from island ID one, to island ID 2.
	 * 
	 * @param from the island ID of the start island
	 * @param to the island ID of the end island
	 * @return Image the image sprite from island `from` to island `to`.
	 * 
	 */
	public static Image getPathImage(int from, int to) {
		String key = ("path" + to) + from;
		if (!paths.containsKey(key)) {
			throw new IllegalArgumentException("Unknown path image requested: " + key);
		}
		return paths.get(("path" + to) + from);
	}
	
	/**
	 * randomly generates island prices
	 */
	public static void setPrices() {
		sellingData = Rand.generatePrices();
		buyingData = Rand.modifyPrices(sellingData, 0.1);
	}
	
	/**
	 * Queries to find the sell price of an item, on a specific island
	 * @param island the target island
	 * @param item the target item
	 * 
	 * @return The sell price of the item
	*/
	public static int getSellPrice(int island, int item) {
		return sellingData[island][item];
	}
	
	
	/**
	 * 	Queries to find the buying price of an item, on a specific island
	 * 
	 * @param island the target island
	 * @param item the target item
	 * 
	 * @return The buy price of item
	*/
	public static int getBuyPrice(int island, int item) {
		return buyingData[island][item];
	}
	
	
	public Image getPath01() {
		return path01;
	}
	
	public Image getPath12() {
		return path12;
	}
	
	public Image getPath02() {
		return path02;
	}
	
	public static Image getEmpty() {
		return empty;
	}
	
	public Button getIslandButton0() {
		return islandButton0;
	}
	
	public Button getIslandButton1() {
		return islandButton1;
	}
	
	public Button getIslandButton2() {
		return islandButton2;
	}

	public static Image getPirateEventMessage1() {
		return pirateEventMessage1;
	}

	public static Image getPirateEventMessage2() {
		return pirateEventMessage2;
	}

	public static Image getPirateEventMessage3() {
		return pirateEventMessage3;
	}

	public static Image getWeatherEventMessage() {
		return weatherEventMessage;
	}

	public static Image getAbandonedShipMessage() {
		return abandonedShipMessage;
	}


	public static Image getNoMoneyMessage() {
		return noMoneyMessage;
	}

	public static Image getNoSpaceMessage() {
		return noSpaceMessage;
	}

	public static Image getNoItemsMessage() {
		return noItemsMessage;
	}

	public static Image getRepairError() {
		return repairError;
	}

	public static Image getShopButton() {
		return shopButton;
	}

	public static Image getInventoryButton() {
		return inventoryButton;
	}

	public static Image getPriceInfoButton() {
		return priceInfoButton;
	}

	public static Image getGameOverMoney() {
		return gameOverMoney;
	}

	public static Image getGameOverPirates() {
		return gameOverPirates;
	}

	public static Image getGameOverGood() {
		return gameOverGood;
	}

	public static Image getGameOverHull() {
		return gameOverHull;
	}

	public Image getPath03() {
		return path03;
	}

	public Image getPath04() {
		return path04;
	}

	public Image getPath13() {
		return path13;
	}

	public Image getPath14() {
		return path14;
	}

	public Image getPath23() {
		return path23;
	}

	public Image getPath24() {
		return path24;
	}

	public Image getPath34() {
		return path34;
	}

	public Button getIslandButton3() {
		return islandButton3;
	}

	public Button getIslandButton4() {
		return islandButton4;
	}
	
	 @Test
	    private void hashTest() {
	        Set<String> keys = paths.keySet();
	        for (String str : keys) {
	            int a1 = (int) str.charAt(str.length() - 2) - '0';
	            int a2 = (int) str.charAt(str.length() - 1) - '0';
	            
	            if (a1 == a2) {
	                fail("Path added to path hash had same end location");
	            }
	        }
	    }
}
