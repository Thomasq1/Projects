package application;

public class recordcontroller {
	private recordlist r1;
	
	public recordcontroller() {
		r1 = new recordlist();
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

}
