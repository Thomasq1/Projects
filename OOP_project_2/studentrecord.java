package application;

public class studentrecord {
	private String details;
	private String modulename;
	private String grade;
	
	public studentrecord(String d, String m, String g) {
		details = d;
		modulename = m;
		grade = g;
	}

	public String getDetails() {
		return details;
	}

	public void setDetails(String details) {
		this.details = details;
	}

	public String getModulename() {
		return modulename;
	}

	public void setModulename(String modulename) {
		this.modulename = modulename;
	}

	public String getGrade() {
		return grade;
	}

	public void setGrade(String grade) {
		this.grade = grade;
	}
	
	public String toString() {
		String s = details + " " + "Module: " + modulename + " " + "Grade : " + grade + "\n";
		return s;
	}
	
	public int gradecompare(studentrecord records) {
		return this.grade.compareTo(getGrade());
	}
	
	public int modulecompare(studentrecord records) {
		return this.modulename.compareTo(records.getModulename());			
	}
		
}

