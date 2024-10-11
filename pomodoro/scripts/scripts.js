// DOM Elements
const minutesDisplay = document.getElementById('minutes');
const secondsDisplay = document.getElementById('seconds');
const startButton = document.getElementById('start');
const pauseButton = document.getElementById('pause');
const resetButton = document.getElementById('reset');
const sessionTracker = document.getElementById('completed-sessions');
const workEndSound = document.getElementById('work-end-sound');
const breakEndSound = document.getElementById('break-end-sound');

let workDuration = 25 * 60; // 25 minutes in seconds
let breakDuration = 5 * 60; // 5 minutes in seconds
let timeRemaining = workDuration; // Initially set to work time
let isWorkSession = true;
let timerInterval; // To store the setInterval reference
let isPaused = true; // To keep track of pause state

// Function to update the timer display
function updateTimerDisplay() {
    let minutes = Math.floor(timeRemaining / 60);
    let seconds = timeRemaining % 60;

    minutesDisplay.textContent = String(minutes).padStart(2, '0');
    secondsDisplay.textContent = String(seconds).padStart(2, '0');
}

// Function to start the timer
function startTimer() {
    if (isPaused) {
        isPaused = false;
        timerInterval = setInterval(function() {
            timeRemaining--;
            updateTimerDisplay();

            // Check if time is up
            if (timeRemaining <= 0) {
                clearInterval(timerInterval);
                isPaused = true;
                switchSession();
            }
        }, 1000);
    }
}

// Function to pause the timer
function pauseTimer() {
    clearInterval(timerInterval);
    isPaused = true;
}

// Function to reset the timer
function resetTimer() {
    clearInterval(timerInterval);
    isPaused = true;
    timeRemaining = isWorkSession ? workDuration : breakDuration;
    updateTimerDisplay();
}

// Function to switch between work and break sessions with sound effects
function switchSession() {
    if (isWorkSession) {
        // Play work end sound
        workEndSound.play();
        timeRemaining = breakDuration;
        isWorkSession = false;
        document.body.style.backgroundColor = "#6ab04c"; // Change to green for break
    } else {
        // Play break end sound
        breakEndSound.play();
        timeRemaining = workDuration;
        isWorkSession = true;
        incrementSessionCount();
        document.body.style.backgroundColor = "#ff6b6b"; // Change to red for work
    }
    updateTimerDisplay();
    startTimer(); // Automatically start the new session
}

// Function to increment the completed Pomodoro session count
function incrementSessionCount() {
    let completedSessions = parseInt(sessionTracker.textContent);
    sessionTracker.textContent = completedSessions + 1;
}

// Event listeners for buttons
startButton.addEventListener('click', startTimer);
pauseButton.addEventListener('click', pauseTimer);
resetButton.addEventListener('click', resetTimer);

// Initial display setup
updateTimerDisplay();
