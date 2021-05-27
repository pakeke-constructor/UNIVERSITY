package main;

import java.util.ArrayList;

/**
 * 
 * Controls player inventory
 * 
 */
public class InventoryHandler {
	private static ArrayList<String[]> purchaseHistory = new ArrayList<String[]>();
	
	/**
	 * Initialize purchase history array as an array of empty strings
	 */
	public static void initPurchaseHistory() {
		for (int i=0;i<7;i++) {
			purchaseHistory.add(new String[10]);
		}
	}
	
	/**
	 * Adds item purchase to purchase history, as a nicely formatted string
	 * 
	 * @param itemID the integer id of the item
	 * @param islandNum the integer id of the island to buy from
	 * @param price the price of the item from the island
	 */
	public static void itemPurchased(int itemID, int islandNum, int price) {
		shuffle(itemID);
		String[] tempStrArray = purchaseHistory.get(itemID);
		tempStrArray[0] = "- " + Integer.toString(price) + "   " + Integer.toString(islandNum);
		purchaseHistory.set(itemID, tempStrArray);
	}
	
	/**
	 * 	@param itemID the integer id of the item
	 *  @param islandNum the integer id of the item to sell from
	 *  @param 
	 */
	public static void itemSold(int itemID, int islandNum, int price) {
		shuffle(itemID);
		String[] tempStrArray = purchaseHistory.get(itemID);
		tempStrArray[0] = "+ " + Integer.toString(price) + "   " + Integer.toString(islandNum);
		purchaseHistory.set(itemID, tempStrArray);
	}
	
	/**
	 * @param itemID the integer id of the item that should be added to purchase history
	 * Pushes a new buy item onto the purchase history
	 */ 
	public static void shuffle(int itemID) {
		String[] tempStrArray = purchaseHistory.get(itemID);
		for (int i=tempStrArray.length-1; i >= 1; i--) {
			tempStrArray[i] = tempStrArray[i-1];
		}
		purchaseHistory.set(itemID, tempStrArray);
	}
	
	public static ArrayList<String[]> getPurchaseHistory() {
		return purchaseHistory;
	}
}
