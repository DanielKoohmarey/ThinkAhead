/* On page load, run the following code. */
$(document).ready(function(){

/* 
Connects individual sortable lists with each other.
Reference: http://devheart.org/articles/jquery-customizable-layout-using-drag-and-drop/
*/
var selector;
for (var i = 0; i < numPlanners; i++) {
	selector = '#planner' + (i + 1);
	$(selector).sortable({
		connectWith: '.sortableList'
	});
}

for (var i = 0; i < numReqs; i++) {
	selector = '#req' + (i + 1);
	$(selector).sortable({
		connectWith: '.sortableList'
	});
}

});