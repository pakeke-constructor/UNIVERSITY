

interface Pos {
	default double distance(double X, double Y, double Z){
		double X2 = (this.x-X)*(this.x-X);
		double Y2 = (this.y-Y)*(this.y-Y);
		double Z2 = (this.z-Z)*(this.z-Z);
		return Math.pow(X2 + Y2 + Z2, 0.5f);
	}

	default double distance(int X, int Y, int Z){
		double X2 = (this.x-X)*(this.x-X);
		double Y2 = (this.y-Y)*(this.y-Y);
		double Z2 = (this.z-Z)*(this.z-Z);
		return Math.pow(X2 + Y2 + Z2, 0.5f);
	}

	default double distance(float X, float Y, float Z){
		double X2 = (this.x-X)*(this.x-X);
		double Y2 = (this.y-Y)*(this.y-Y);
		double Z2 = (this.z-Z)*(this.z-Z);
		return Math.pow(X2 + Y2 + Z2, 0.5f);
	}

	default double setPos(double X, double Y, double Z){
		this.x=X; this.y=Y; this.z=Z;
	}

	default double setPos(int X, int Y, int Z){
		this.x=(double)X; this.y=(double)Y; this.z=(double)Z;
	}
	
	default double setPos(float X, float Y, float Z){
		this.x=(double)X; this.y=(double)Y; this.z=(double)Z;
	}
}



class Dude implements Pos {
	String hi;

	double x;
	double y;
	double z;


	public Dude(){
		hi = "hello world";
	}

	public void sayHello(){
		System.out.println(x);
		setPos(933,2,3);
		System.out.println(x);
	}
}



