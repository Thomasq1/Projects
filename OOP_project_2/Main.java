//Thomas O'Brien R00192530
package application;

//imports needed for functionality
import javafx.scene.control.DatePicker;

import java.util.ArrayList;
import javafx.application.Application;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.EventHandler;
import javafx.geometry.Pos;
import javafx.geometry.Side;
import javafx.event.ActionEvent;
import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.ComboBox;
import javafx.scene.control.Label;
import javafx.scene.control.Tab;
import javafx.scene.control.TabPane;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;
import javafx.scene.layout.VBox;
import javafx.scene.paint.Color;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.HBox;
import javafx.stage.Stage;



public class Main extends Application{
	//constructors
	private Stage window;
	private static Label namelabel;
	private static Label IDlabel;
	private static Label DOBlabel;
	private static Label ModuleLabel;
	private static Label GradeLabel;
	private static Label DDLabel;
	private static Label DDLabel2;
	private static TextArea studentDetails;
	private static TextArea studentRecords;
    private static  Button      addButton, removeButton, listButton, loadbutton, savebutton, exitbutton, clearbutton, addgradebutton, viewbutton, gradeorder, moduleorder;
    private static Controller StudentController = new Controller();
    private ObservableList<student> studentObservableList;
   
    
   
    public static void main(String[] args) {
	   launch(args);
	   }
	
	@Override
	public void start(Stage primaryStage) throws Exception {
		ArrayList<student> studentArrayList = new ArrayList<>();
        this.studentObservableList = FXCollections.observableList(studentArrayList);
        
		window = primaryStage;
		//StudentController.loadfile(StudentController.getstudents().getStudentlist());	
	    //setting the title of the gui window
	    window.setTitle("MTU Student Record System");
	    //new label
	    namelabel = new Label("Enter Name: ");
	    //textfield for the name field
	    TextField tf = new TextField();
	    
	    //listener that will not allow the user to enter numbers into the name field reducing potential error
	    tf.textProperty().addListener((observable, oldValue, newValue) -> {
	        if (!newValue.matches("\\sa-zA-Z*")) {
	            tf.setText(newValue.replaceAll("[^\\sa-zA-Z]", ""));
	        }
	    });
	    IDlabel = new Label("Enter ID: ");
	    TextField tf2 = new TextField();  
	    int max = 9;
	    //another listener i setup that will not allow the ID entered to be longer than 9 characthers 
	    tf2.textProperty().addListener((observable, oldValue, newValue) -> {
	    	if(newValue.length() > max) {
	    		oldValue = oldValue.substring(0, max);	 
	    		tf2.setText(oldValue);
	    	}
	    });
	    DOBlabel = new Label("Enter Date Of Birth DD/MM/YYYY : ");
	    //datepicker i setup to make cohhins the date easier and less error prone
	    DatePicker D1 = new DatePicker();
	    //set the datepicker field as uneditable as there is no need for the user that change the contents
	    D1.setEditable(false);
	    
	    //addbutton to implemmtn the add function once pressed
	    addButton = new Button("Add");
	    //action event to give the button functionality
	    addButton.setOnAction(e-> {
	    	//if statemnts to stop data being entered to the arraylist if not all 3 fields are filled
	    	if(tf.getText().isEmpty()) {
	    		studentDetails.setText("Please fill in all 3 fields before adding! ");
	    	} else if(tf2.getText().isEmpty()) {
	    		studentDetails.setText("Please fill in all 3 fields before adding! ");
	    	} else if(D1.getValue().toString().isEmpty()) {
	    		studentDetails.setText("Please fill in all 3 fields before adding! ");
	    	} else {
	    		try {
	    			//when all 3 fields arew filled correctly the addstudent in the controller is called and executed adding the student to the list
	    			StudentController.addStudenttoList(tf.getText(), tf2.getText(), D1.getValue().toString());
	    			//clearing the textfields and datepicker once the data has been added
			    	tf.setText("");
			    	tf2.setText("");
			    	D1.setValue(null);
			    	studentDetails.setText("");
	    		}
	    		catch(Exception e1) {
	    			e1.printStackTrace();
	    		}
	    	}
	    	
	    	});
	    //button to clear the datepicker in the event the user enter a incorrect date
	    clearbutton = new Button("Clear DatePicker");
	    clearbutton.setOnAction(e -> D1.setValue(null));
	    //remove button that executes the remove user function
	    removeButton = new Button("Remove");
	    removeButton.setOnAction(e-> StudentController.removestudentfromlist(tf.getText()));
	    
	    listButton = new Button("List");
	    listButton.setOnAction(new EventHandler<ActionEvent>() {
	    	//list button that implemtns the listuser function when pressed
	    @Override
	    public void handle(ActionEvent event) {
	    	String studentList=StudentController.getstudentlist();
	    	studentDetails.setText(studentList);
	    }
	    	
	    });
	    //textarea to display user details and system messages
	    studentDetails = new TextArea("Details");
	    studentDetails.setEditable(false);
	    
	    loadbutton = new Button("Load");
	    loadbutton.setOnAction(e -> {
	    	StudentController.load();
    	//StudentController.loadfile(StudentController.getstudents().getStudentlist());	
	    
	    });
	    savebutton = new Button("Save");
	    savebutton.setOnAction(e -> { 
	    //	StudentController.saveFile();
	    	StudentController.save(new ArrayList<>(this.studentObservableList));
	    });
	    //exit button that will display a popup asking the user are they sure they want to eixt and a option to save their work
	    exitbutton = new Button("Exit");
	    exitbutton.setOnAction(e -> {
	    	popup.display("Exit", "Do you want to save before exiting? ");
	    	
	    });
	    //hboxes and vbox to display all the gui elemnts to the scene
	    HBox h1 = new HBox(10);
	    h1.getChildren().addAll(namelabel, tf);
	    h1.setAlignment(Pos.BASELINE_CENTER);
	    HBox h2 = new HBox(10);
	    h2.getChildren().addAll(IDlabel, tf2);
	    h2.setAlignment(Pos.BASELINE_CENTER);
	    HBox h3 = new HBox(10);
	    h3.getChildren().addAll(DOBlabel, D1, clearbutton);
	    h3.setAlignment(Pos.BASELINE_CENTER);
	    HBox h4 = new HBox(10);
	    h4.getChildren().addAll(addButton, removeButton, listButton);
	    
	    HBox h5 = new HBox(10);
	    h5.getChildren().addAll(studentDetails);
	    
	    HBox h6 = new HBox(10);
	    h6.getChildren().addAll(loadbutton, savebutton, exitbutton);
	    
	    VBox v1 = new VBox(10);
	    v1.getChildren().addAll(h1,h2,h3,h4,h5,h6);
	    
	    Group root = new Group();   
	    TabPane tabPane = new TabPane();     
		BorderPane mainPane = new BorderPane(); 
		Scene scene = new Scene(root, 540, 440, Color.WHITE);
		tabPane.setSide(Side.TOP);
		//tab to adding students so part 1 stuff
		Tab AddStudent = new Tab("Add Student");
		AddStudent.setClosable(false);
		AddStudent.setContent(v1);
		tabPane.getTabs().add(AddStudent);
		
		//2nd tab for recording modules
		DDLabel = new Label("Select a student : ");
		String studentList2 = StudentController.getstudentlist();
		ComboBox<String> combobox = new ComboBox<>();		
		combobox.setVisibleRowCount(3);
		combobox.setPromptText("Select Student: ");
		String[] list = studentList2.split(",");
		for(String s : list) {
			combobox.getItems().add(s);
		}
		ModuleLabel = new Label("Module Name : ");
		TextField tf3 = new TextField();
		GradeLabel = new Label("Grade : ");
		TextField tf4 = new TextField();
		addgradebutton = new Button("Add grade");
		addgradebutton.setOnAction(e -> {
			StudentController.addrecordtolist(combobox.getValue().toString(), tf3.getText(), tf4.getText());
			
		});
		
		HBox h7 = new HBox(10);
		h7.getChildren().addAll(DDLabel, combobox);
		
		HBox h8 = new HBox(10);
		h8.getChildren().addAll(ModuleLabel, tf3);		
		
		HBox h9 = new HBox(10);
		h9.getChildren().addAll(GradeLabel, tf4);
		
		HBox h10 = new HBox(10);
		h10.getChildren().addAll(addgradebutton);
		
		VBox v2 = new VBox(10);
		v2.getChildren().addAll(h7,h8,h9,h10);
		
		
		Tab RecordStudent = new Tab("Record Student Modules");
		RecordStudent.setClosable(false);
		RecordStudent.setContent(v2);
		tabPane.getTabs().add(RecordStudent);
		
		
//		TextField tf5 = new TextField();
		DDLabel2 = new Label("Select a student (ID) : ");
		studentRecords = new TextArea("Student Records ");
		studentRecords.setEditable(false);
		studentRecords.setPrefWidth(500);
		ComboBox<String> combobox2 = new ComboBox<>();		
		combobox2.setVisibleRowCount(3);
		combobox2.setPromptText("Select Student: ");
		String[] list2 = studentList2.split(",");
		for(String s : list2) {
			combobox2.getItems().add(s);
		}
		viewbutton = new Button("View");
		viewbutton.setOnAction(new EventHandler<ActionEvent>() {
		@Override
		public void handle(ActionEvent event) {
			studentrecord recordlist = StudentController.findstudentrecordsfromlist(combobox2.getValue().toString());
			studentRecords.setText(recordlist.toString());
			}
		});
		gradeorder = new Button("Order by grade");
		gradeorder.setOnAction( e -> {
			StudentController.orderbygrade();
		});
		moduleorder = new Button("Order by module");
		moduleorder.setOnAction( e -> {
			StudentController.orderbymodule();
		});
		
		HBox h11 = new HBox(10);
		h11.getChildren().addAll(DDLabel2, combobox2);
		
		HBox h12 = new HBox(10);
		h12.getChildren().addAll(studentRecords);
		
		HBox h13 = new HBox(10);
		h13.getChildren().addAll(viewbutton,gradeorder,moduleorder);
		
		VBox v3 = new VBox(10);
		v3.getChildren().addAll(h11,h13,h12);
		//3rd tab for displaying all records
		Tab ViewRecords = new Tab("View Student Records");
		ViewRecords.setClosable(false);
		ViewRecords.setContent(v3);
		tabPane.getTabs().add(ViewRecords);
		
	   
	    //creating a scene to display the gui
		mainPane.setCenter(tabPane);
		mainPane.prefHeightProperty().bind(scene.heightProperty());
		mainPane.prefWidthProperty().bind(scene.widthProperty());
		root.getChildren().add(mainPane);
	    window.setScene(scene);
	    window.show();
	       
	}
	
	
}




  