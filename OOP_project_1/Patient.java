import java.util.ArrayList;

public class Patient extends Person {
	ArrayList<Person> List_Of_visits;
	private String illness;
	
	enum severity{
		mild,
		bad,
		verybad,
		reallybad,
		severe
	}
	
	public Patient(String illness, String name, String id, String phone) {
		super(name, id, phone);
		this.illness = illness;
		List_Of_visits = new ArrayList<Person>(100);
	} 
	
	public void addvisit(Person p) {
		List_Of_visits.add(p);
	}
	
	public void showvisits() {
		for (int i = 0; 1 < List_Of_visits.size(); i++) {
			Person visitlist = List_Of_visits.get(i);
			System.out.print(visitlist);
		}
	}
	
	


	public String illnessdescription() {
		return illness;
	}
	
	public void severity() {
		severity level = severity.verybad;
		System.out.print(level);
	}

	public ArrayList<Person> getList_Of_visits() {
		return List_Of_visits;
	}

	public void setList_Of_visits(ArrayList<Person> list_Of_visits) {
		List_Of_visits = list_Of_visits;
	}

	public String getIllness() {
		return illness;
	}

	public void setIllness(String illness) {
		this.illness = illness;
	}
	
	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (!super.equals(obj))
			return false;
		if (getClass() != obj.getClass())
			return false;
		Patient other = (Patient) obj;
		if (List_Of_visits == null) {
			if (other.List_Of_visits != null)
				return false;
		} else if (!List_Of_visits.equals(other.List_Of_visits))
			return false;
		if (illness == null) {
			if (other.illness != null)
				return false;
		} else if (!illness.equals(other.illness))
			return false;
		return true;
	}
	
	public String toString() {
		return this.getName() + " " + this.getId() + " " + this.getPhone() + " " + this.illness + " " +  List_Of_visits;
	}



}
