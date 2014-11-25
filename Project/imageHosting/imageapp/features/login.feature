Feature: User login 
		 I am an existing user to imageSpace
		 I want to log in
	
	Scenario: Log in without email/password
		Given that I hit log in
		Then I should see "This field is required"
	
	Scenario: Log in with email only
		Given that I enter my email
		Then I should see "This field is required"
	
	Scenario: Log in with password only
		Given that I enter my password
		Then I should see "This field is required"
		
	Scenario: Log in with email and invalid password
		Give that I enter the wrong password
		Then I should see "Login Error!"
			
	Scenario: Log in with valid email/password
		Given that I enter a valid email/password
		Then I should see "/home/"
	
	
		
	