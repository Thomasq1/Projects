//Thomas O'Brien R00192530
package application;



public class student {
	private String name;
	private String ID;
	private String DOB;
	
	public student(String n, String i, String d) {
		name = n;
		ID = i;
		DOB = d;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getID() {
		return ID;
	}

	public void setID(String iD) {
		ID = iD;
	}

	public String getDOB() {
		return DOB;
	}

	public void setDOB(String dOB) {
		DOB = dOB;
	}
	
	public String toString() {
		String s = "Student Name: "+ name + " " + "Student ID: " + ID + " " + "Student D.O.B: " + DOB+ "\n"+",";
		return s;
	}

}
