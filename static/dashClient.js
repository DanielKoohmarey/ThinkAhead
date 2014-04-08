$(document).ready(function(){

/* 
Connects individual sortable lists with each other.
Reference: http://devheart.org/articles/jquery-customizable-layout-using-drag-and-drop/
*/
for (var i = 0; i < numPlanners; i++) {
	var selector = '#planner' + (i + 1);
	$(selector).sortable({
		connectWith: '.sortableList'
	});
}

for (var i = 0; i < numReqs; i++) {
	var selector = '#req' + (i + 1);
	$(selector).sortable({
		connectWith: '.sortableList'
	});
}

});