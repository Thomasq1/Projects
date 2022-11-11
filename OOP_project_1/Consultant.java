import java.util.ArrayList;

public class Consultant extends Person {
	ArrayList<Person> List_Of_patients;
	ArrayList<Person> List_Of_visits;
	
	private String expertise;
	
	public Consultant(String expertise, String name, String id, String phone) {
		super(name, id, phone);
		this.expertise = expertise;
		List_Of_patients = new ArrayList<Person>(100);
		List_Of_visits = new ArrayList<Person>(100);
		
	}
	
	public void addpatient(Person p) {
		List_Of_patients.add(p);
	}
	
	public void addvisit(Person p) {
		List_Of_visits.add(p);
	}
	
	public void showpatients() {
		for (int i = 0; 1 < List_Of_patients.size(); i++) {
			Person patientlist = List_Of_patients.get(i);
			System.out.print(patientlist);
		}
	}
	
	public void showpatientsandvisits() {
		for (int i = 0; 1 < List_Of_patients.size() && 1 < List_Of_visits.size(); i++) {
			Person patientlist = List_Of_patients.get(i);
			Person visitlist = List_Of_visits.get(i);
			System.out.print(patientlist);
			System.out.print(visitlist);
		}
	}
	
	



	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (!super.equals(obj))
			return false;
		if (getClass() != obj.getClass())
			return false;
		Consultant other = (Consultant) obj;
		if (List_Of_patients == null) {
			if (other.List_Of_patients != null)
				return false;
		} else if (!List_Of_patients.equals(other.List_Of_patients))
			return false;
		if (List_Of_visits == null) {
			if (other.List_Of_visits != null)
				return false;
		} else if (!List_Of_visits.equals(other.List_Of_visits))
			return false;
		if (expertise == null) {
			if (other.expertise != null)
				return false;
		} else if (!expertise.equals(other.expertise))
			return false;
		return true;
	}

	public ArrayList<Person> getList_Of_patients() {
		return List_Of_patients;
	}

	public void setList_Of_patients(ArrayList<Person> list_Of_patients) {
		List_Of_patients = list_Of_patients;
	}

	public ArrayList<Person> getList_Of_visits() {
		return List_Of_visits;
	}

	public void setList_Of_visits(ArrayList<Person> list_Of_visits) {
		List_Of_visits = list_Of_visits;
	}

	public String getExpertise() {
		return expertise;
	}

	public void setExpertise(String expertise) {
		this.expertise = expertise;
	}
	
	public String toString() {
		return this.getName() + " " + this.getId() + " " + this.getPhone() + " " + this.expertise + " " + List_Of_patients + " " + List_Of_visits;
	}
	
	
	

}
