package main;

import java.awt.Graphics;
import java.awt.Image;

/**
 * Base class that other objects inherit from.
 * 
 */
public class GameObject {
	private Image img;
	private int x;
	private int y;
	
	/**
	 * @param imgSprite the image the object takes
	 * @param posX x position
	 * @param posY y position
	*/
	public GameObject(Image imgSprite, int posX, int posY) {
		img = imgSprite;
		x = posX;
		y = posY;
	}
	
	/**
	 * changes gameObject image.
	 * @param image the new sprite to change to
	 */
	public void setImage(Image image) {
		img = image;
	}
	
	/**
	 * getter for GameObject's image
	 * @return the gameObject's image.
	 */
	public Image getImage() {
		return img;
	}
	
	/**
	 *  @return X position
	 */
	public int getX() {
		return x;
	}
	
	/**
	 *  @return Y position
	 */
	public int getY() {
		return y;
	}
	
	/**
	 *  @param newX sets x position to this
	 */
	public void setX(int newX) {
		x = newX;
	}
	
	/**
	 *  @param newY sets y position to this
	 */
	public void setY(int newY) {
		y = newY;
	}
	
	/**
	 * draws the object at position x, y, with specified image.
	 * @param graphics The graphics pipeline object
	 * @param window the JFrame GameLogic window
	 */
	public void draw(Graphics graphics, GameLogic window) {
		graphics.drawImage(img, x, y, window);
	}
}







