package application;

import java.util.ArrayList;

public class recordlist {
	private ArrayList<studentrecord> records;
	public recordlist() {
		records = new ArrayList<studentrecord>();
	}
	
	public ArrayList<studentrecord> getrecordlist() {
		return records;
	}
	
	public void addRecord(studentrecord r) {
		records.add(r);
	}
	
	public int getrecordsize() {
		return records.size();
	}
	
	public studentrecord getrecord(int i) {
		if ((i>-1 && i<records.size()))
			return records.get(i);
		return null;
	}
	
	public studentrecord findrecordswithID(String details) {
		for (int i = 0;i<records.size();) {
			studentrecord recordList = records.get(i);
			String studentid = recordList.getDetails();
			if(studentid.contains(details))
			return recordList;
			
		}
		return null;
		
	}

}
