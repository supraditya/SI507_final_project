function hoverShow(nodeId) {
    // Function shows the container with the commit message when user hovers onto the commit node
  commitNode = document.getElementById(nodeId);
  infoContainerId = "node-info-" + nodeId;
  commitInfoContainer = document.getElementById(infoContainerId);
  commitInfoContainer.style.display = "block";
}
function hoverHide(nodeId) {
    // Function hides the container with the commit message when user hovers away from the commit node
  commitNode = document.getElementById(nodeId);
  infoContainerId = "node-info-" + nodeId;
  commitInfoContainer = document.getElementById(infoContainerId);
  commitInfoContainer.style.display = "none";
}

function createLines(parentnodeId) {
//   Function basically gets the IDs of the parent commit node and that of all of its children, and then iteratively draws
// SVG lines from parent to the the child


  parentNode = document.getElementById(parentnodeId); //Getting the coordinate position of the parent commit node
  parentNode_data = parentNode.getBoundingClientRect();
  parent_x = parentNode_data.x;
  parent_y = parentNode_data.y; 

  //Getting the list of childnode IDS. Solution is hacky because Flask does not have
  //A reliable way of passing lists into a javascript function
  //Basically getting the name attribute of the parent node (that I injected with the list of children) using outerHTML
  //Using string operations to removes quotes and then creating a list out of the ids, thus giving me the list of children
  //nodes

  str = parentNode.outerHTML; 
  str_start = str.search("name");
  str_end = str.lastIndexOf(" ");
  str_slice = str.substring(str_start, str_end);
  str_slice = str_slice.substring(8, str_slice.length - 3);
  // Opening quote removal
  str_slice = str_slice.replace("'", "");
  // Closing quote removal
  str_slice = str_slice.replace("'", "");
  // Removing whitespaces
  str_slice = str_slice.replace(" ", "");
  children = str_slice.split(",");


  var svg = document.getElementById("svg-canvas");

    //   Drawing SVG lines from parent to each child
  children.forEach((childId) => {
    childNode = document.getElementById(childId);

    // To avoid triggering an error if the node is a leaf node i.e. without any children
    if (childNode !== null) {
      childNode_data = childNode.getBoundingClientRect();
      child_x = childNode_data.x;
      child_y = childNode_data.y;

    //   Checking if line is already rendered to avoid redrawing
      var line = document.getElementById(parentnodeId + childId);
      if (line === null) {
        line = document.createElementNS("http://www.w3.org/2000/svg", "line");
        line.id = parentnodeId + childId;
        line.setAttribute("x1", parent_x + 20);
        line.setAttribute("y1", parent_y - 120);
        line.setAttribute("x2", child_x + 20);
        line.setAttribute("y2", child_y - 120);
        line.setAttribute("stroke", "black");
        svg.appendChild(line);
        console.log("Added!");
      }
    }
  });

}
function svgSizer() {
  //This function adjusts the size of the SVG div to that of the graph div
  var svg = document.getElementById("svg-canvas");
  var graph = document.getElementById("graph");
  g_height = graph.clientHeight;
  g_width = graph.clientWidth;
  svg.setAttribute("width", g_width);
  svg.setAttribute("height", g_height);
}
