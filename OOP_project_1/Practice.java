import java.util.ArrayList;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Practice {
	ArrayList<Person> List_Of_Consultants;
	ArrayList<Person> List_Of_patients;
	private String Name;
	private String id;
	
	
	

	
	

	public Practice(String name, String patientId) {
		this.id = patientId;
		List_Of_Consultants = new ArrayList<Person>(100);
		List_Of_patients = new ArrayList<Person>(100);
	}
	
	public void addconsultant(Person p) {
		List_Of_Consultants.add(p);
	}
	
	public void showconsultantlist() {
		for (int i = 0; 1 < List_Of_Consultants.size(); i++) {
			Person consultantlist = List_Of_Consultants.get(i);
			System.out.print(consultantlist);
		}
	}
	
	public Person findconsultant(String Name) {
		for (int i = 0; i < List_Of_Consultants.size(); i++) {
			Person consultantlist = List_Of_Consultants.get(i);
			String consultantname = consultantlist.getName();
			if (consultantname.equals(Name)) {
				return consultantlist;
			}
		
		}
		return null;
		
	}
	
	public Person findpatient(String Name) {
		for (int i = 0; i < List_Of_patients.size(); i++) {
			Person patientlist =  List_Of_patients.get(i);
			String patientname = patientlist.getName();
			if (patientname.equals(Name)) {
				return patientlist;
			}
		}
		return null;
	}
	
	public void showallconsultants(String Name, int id) {
		 try {
		      File myObj = new File("Practice.txt");
		      Scanner myReader = new Scanner(myObj);
		      while (myReader.hasNextLine()) {
		        String data = myReader.nextLine();
		        System.out.println(data);
		      }
		      myReader.close();
		    } catch (FileNotFoundException e) {
		      System.out.println("An error occurred.");
		      e.printStackTrace();
		    }
	}

	public String getName() {
		return Name;
	}

	public void setName(String name) {
		Name = name;
	}

	public String getId() {
		return id;
	}

	public void setId(String id) {
		this.id = id;
	}
	
	public String toString() {
		return Name + " " + id + " " + List_Of_Consultants + " " + List_Of_patients;
	}
	
	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Practice other = (Practice) obj;
		if (List_Of_Consultants == null) {
			if (other.List_Of_Consultants != null)
				return false;
		} else if (!List_Of_Consultants.equals(other.List_Of_Consultants))
			return false;
		if (List_Of_patients == null) {
			if (other.List_Of_patients != null)
				return false;
		} else if (!List_Of_patients.equals(other.List_Of_patients))
			return false;
		if (Name == null) {
			if (other.Name != null)
				return false;
		} else if (!Name.equals(other.Name))
			return false;
		if (id == null) {
			if (other.id != null)
				return false;
		} else if (!id.equals(other.id))
			return false;
		return true;
	}
	
	
	

	
	
	
	
	
}

