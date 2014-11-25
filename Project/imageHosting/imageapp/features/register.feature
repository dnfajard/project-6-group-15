Feature: User registration
		 I am a new user to imageSpace
		 I want to create an account so that I can login
	

	Scenario: Register with one or more fields not filled
		Given that I hit register now with one or more fields not filled
		Then I should see "This field is required." at the empty field
	
	Scenario: Register without all fields filled
		Given that I hit register now without all fields filled
		Then I should see "This field is required."
		
	Scenario: Register with existing email only
		Given that I enter an existing email only
		Then I should see "User with this email already exists" and "This field is required."
		
	Scenario: Register with non-existing email and all fields filled
		Given that I hit register now with a non-existing email and all fields are filled
		Then I should see "Registration success. Proceed to login"
	
