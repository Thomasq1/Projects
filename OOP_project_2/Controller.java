//Thomas O'Brien R00192530
package application;

import java.io.*;
import java.util.ArrayList;

import javafx.collections.ObservableList;
//import java.util.Date;
 //import javafx.scene.control.DatePicker;

public class Controller {
	private studentlist s1;
	private recordlist r1;



    public Controller() {
    	//adding the arraylist
    	s1 = new studentlist();
    	r1 = new recordlist();
    }
    
    public studentlist getstudents() {
    	return s1;
    }
    
    //function that takes 3 parameters which are the textifled and datepicker and adds the student
    public void addStudenttoList(String name, String ID, String DOB) {
    	student s = new student(name, ID, DOB);
    	s1.addStudent(s);
    	
    }

    public void remove(studentrecord records) {
    	r1.getrecordlist().remove(records);
    }
    
    
    //executes the remove function in the studentlist class
    public void removestudentfromlist(String s) {
    	s1.removestudentwithName(s);
		
    }
    //function that list out each student in the array by iterating through until no more are left
    public String getstudentlist() {
    	String studentList = "";
    	for(int i = 0;i<s1.getstudentsize();i++) {
    		studentList = studentList + s1.getstudent(i);
    	}
    	return studentList;
    	
    }
   
    	
    
    
    
   public String findstudentfromlist(String id) { 
	   s1.findstudentwithID(id);
	return id;
   }
    
   public void saveFile() {
	   try {
		   PrintWriter output = new PrintWriter("C:/stuff/college/OOP/StudentRecords.txt");
		   ArrayList<student> iterablelist = s1.getStudentlist();
		   for(student s: iterablelist)
			   output.println(s.getName() + "," + s.getID() + "," + s.getDOB());
		   output.close();
		   System.out.println("File Saved");
	   }catch (FileNotFoundException e) {
		   System.out.println("File not found");
	   }
   }
   
   public ArrayList<student> loadfile(ArrayList<student> s1) {
	   try {
		   FileReader filereader = new FileReader("C:/stuff/college/OOP/StudentRecords.txt");
		   BufferedReader inputfile = new BufferedReader(filereader);
		   String line = inputfile.readLine();
		   s1.clear();
		   while(line != null) {
			   String[] data = line.split(",");
			   s1.add(new student(data[0], data[1], data[2]));
			   line = inputfile.readLine();
		   }
		   inputfile.close();
		   System.out.println("File loaded");
	   }catch(IOException e) {
		   e.printStackTrace();
	   }
	   return s1;
   }
   
   public recordlist getrecords() {
		return r1;
   }
   
   public void addrecordtolist(String details, String module, String grade) {
		studentrecord r = new studentrecord(details, module, grade);
		r1.addRecord(r);
	}
   
   public String getrecordlist() {
		String recordList = "";
		for(int i = 0;i<r1.getrecordsize();i++) {
			recordList = recordList + r1.getrecord(i);
		}
		return recordList;
	}
   
   public studentrecord findstudentrecordsfromlist(String details) { 
	   for(int i = 0;i<r1.getrecordsize();) {
		   studentrecord recordList = r1.getrecord(i);
		   String studentid = recordList.getDetails();
		   if(studentid.equals(details))
			   return recordList;
	   }
	return null;
	
	
   }
   
   public void orderbygrade() {
	   ArrayList<studentrecord> recordlist = new ArrayList<>(r1.getrecordlist());
	   while(r1.getrecordlist().size() > 0) {
		   remove(r1.getrecordlist().get(0));
		   
	   }
	   recordlist.sort(studentrecord::gradecompare);
	   for (studentrecord records : recordlist) {
		   r1.addRecord(records);
	   }
   }
	   public void orderbymodule() {
		   ArrayList<studentrecord> recordlist = new ArrayList<>(r1.getrecordlist());
		   while(r1.getrecordlist().size() > 0) {
			   remove(r1.getrecordlist().get(0));  
		   }
		   recordlist.sort(studentrecord::modulecompare);
		   for (studentrecord records : recordlist) {
			   r1.addRecord(records);
		   }
	
   }
	   
   public void save(ArrayList<student> studentArrayList) {
	   try {
		   ObjectOutputStream objectOutputStream = new ObjectOutputStream(new FileOutputStream("C:/stuff/college/OOP/Students.txt"));
		   objectOutputStream.writeObject(studentArrayList);
		   System.out.println("Saved!");
		   objectOutputStream.close();
	   }catch (IOException e) {
		   e.printStackTrace();
	   }
   }
   
   public void load() {
	   try {
		   ObjectInputStream objectInputStream = new ObjectInputStream(new FileInputStream("C:/stuff/college/OOP/Students.txt"));
           ArrayList arrayList = (ArrayList) objectInputStream.readObject();
           ArrayList<student> studentArrayList = new ArrayList<>();
           for(Object array : arrayList) {
        	   if(array instanceof student) {
        		   studentArrayList.add((student) array);
        	   }
           }
           if (studentArrayList.size() == 0) {
        	   System.out.println("No data to save!");
           }
           System.out.println("Loaded!");
           ObservableList<student> studentlist = s1.getoblist();
           studentlist.addAll(studentlist);
           objectInputStream.close();
	   }catch(IOException e) {
		   e.printStackTrace();
	   } catch (ClassNotFoundException e) {
		e.printStackTrace();
	}
   }
   
   
    
    

}