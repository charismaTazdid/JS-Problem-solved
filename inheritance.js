// Create and define Adult.
function Adult() {}
Adult.prototype.speak = function(){
  alert ('I am an adult!');
};
Adult.prototype.workDay= function(){
  alert ('I have to go to work.');
};
// Create and define Student.
function Student() {
  // Call the Adult function.
  Adult.call(this);
}
// Tell Student to inherit Adult.
Student.prototype = new Adult();
Student.prototype.constructor = Student;
// Change the workDay method.
Student.prototype.workDay= function(){
  alert('I have to do my homework.');
}
// add speakGoodbye method
Student.prototype.speakGoodbye= function(){
  alert('I am going to the library. Goodbye.');
}
var studentA = new Student();
studentA.workDay();
studentA.speak();
studentA.speakGoodbye();
// To check for inheritance:
alert(studentA instanceof Adult);
// Returns true.
alert(studentA instanceof Student);
// Returns true.