//Thomas O'Brien R00192530
package application;

import java.util.ArrayList;

import javafx.collections.ObservableList;
//import java.io.*;


public class studentlist {
	//private String name;
	//private String ID;
	//private Date DOB;
	//Create arraylist students
	private ObservableList<student> studentoblist;
	private ArrayList<student> students;
	public studentlist() {
		students = new ArrayList<student>();
	}
	//getter
	public ArrayList<student> getStudentlist() {
		return students;
	}
	//function to add the student
	public void addStudent(student s) {
		students.add(s);
	}
	//function to get a student from the arraylist
	public student getstudent(int i) {
		if ((i>-1 && i<students.size()))
			return students.get(i);
		return null;
	}
	//function that uses the getstudent above it to find the student to be removed and executes
	public void removestudentwithName(String s) {
		for (int i = 0 ; i< students.size(); i++)
			if (getstudent(i).getName().equals(s))
			    students.remove(i);
	}
	
	public student findstudentwithID(String id) {
		for (int i = 0 ; i< students.size();) {
			student studentlist = students.get(i);
			String studentid = studentlist.getID();
			if(studentid.equals(id));
			
			return studentlist;
			
	}
	return null;
}
	//returns the size of the arraylist
	public int getstudentsize() {
		return students.size();
	}
	
	ObservableList<student> getoblist() {
		return studentoblist;
	}
}
