**Environment where the bug occurred:**

- **Hardware environment:** Convergence Airframe
- **Software environment:** gps+HereFlow, USB disabled to have enough RAM left (without airspeed sensor), Forward Thrust enabled
- **Report Time:** Jul 14, 2021
- **PX4 Autopilot commit version:** not mentioned
- **last commit before the reporting time:**7f2acb6

**Steps for bug reproduction:**

- **Step 1:** Use Convergence Airframe
- **Step 2:** Utilize gps+HereFlow
- **Step 3:** Disable USB to have enough RAM left (without airspeed sensor)
- **Step 4:** Enable Forward Thrust
- **Step 5:** Ensure enough wind to enable weathervane
- **Step 6:** Initiate start position, mission, or RTL

**Observed behavior by the user:**

- **Behavior after step 6:** Weathervane does not function as expected, contrary to its performance in version 1.11 with the same setup.

**Expected behavior:**

- **Expected behavior 1:** Weathervane should operate and turn the aircraft into the wind from a slight roll inclination.

**Additional information provided by the user for bug investigation:**

- **Actions taken by the user:** Investigated the logic in code related to lateral movements and weathervane activation; attempted changes in version 1.12.1 for testing in pos mode.
- **URL of the flight log provided by the user:** [Flight log](https://review.px4.io/plot_app?log=a8f081af-ee68-42a0-81e4-71768cec0ed2)

**Communication between developers or other personnel and the user:**

- **Suggestion 1 provided by developers or other personnel:** RomanBapst pointed out the removal of weathervane support for position control flight mode and interjected that it should still work in RTL.
- **Result of the operation after the user adopted suggestion 1:** Taileron noted potential safety improvements if weathervane functioned in pos mode.
  
- **Suggestion 2 provided by developers or other personnel:** Dagar mentioned implementing a yaw handler for FlightTaskManualAcceleration.
- **Result of the operation after the user adopted suggestion 2:** Taileron modified two lines of code and reported successful testing of weathervane in pos mode under version 1.12.1, with plans to test version 1.13.0.
