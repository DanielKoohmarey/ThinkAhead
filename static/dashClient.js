/*
Bound to 'Save Planner Button. 
Makes a POST request to save current planners state represented as list of lists.
*/
function savePlanners() {
	var planners = getPlanners();
	$.post( "/dashboard/", { 'planners[]': planners } );
        window.setTimeout(function() {
            location.reload(true);
        }, 500);
      
}

/*
Called by savePlanners().
Captures and returns current state of planners as list of lists.
*/
function getPlanners() {
	var planners = [];
	var currId;
	for (var i = 0; i < numPlanners; i++) {
		currId = '#planner' + (i + 1);
		var courses = [];
		$(currId + ' li').each(function(i) {
			courses.push($(this).text());
		});
		planners.push(courses);
	}
	return planners;
}

/* On page load, run the following code. */
$(document).ready(function(){

/*
Sets up collaspible requirements list.
Modified from:
http://stackoverflow.com/questions/12480838/use-jquery-to-expand-collapse-ul-list-having-problems
*/
$('.reqComplete ul').hide();
$('.reqComplete .reqDescription').hide();

$('.reqTitle').click(function() {
    $(this).parent().find('ul').slideToggle();
    $(this).parent().find('.reqDescription').slideToggle();
});

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