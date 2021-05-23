package main;

public class Button {
	/*
	Represents the button class
	*/
	private int minX;
	private int maxX;
	private int minY;
	private int maxY;
	
	public Button(int x1, int x2, int y1, int y2) {
		/*
		@param x1 the left position of button
		@param y1 the bottom position of button
		@param x2 the right position of button
		@param y2 the top position of button
		*/
		minX = x1;
		maxX = x2;
		minY = y1;
		maxY = y2;
	}
	
	public boolean pressed(int mouseX, int mouseY) {
		/*
		@param mouseX the position of the mouse in X
		@param mouseY the position of the mouse in Y
		
		@return whether the mouse position was over the button or not
		*/
		return (mouseX > minX && mouseX < maxX && mouseY > minY && mouseY < maxY);
	}
	
}
