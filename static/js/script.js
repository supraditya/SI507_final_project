function hoverShow(nodeId) {
  commitNode = document.getElementById(nodeId);
  infoContainerId = "node-info-" + nodeId;
  commitInfoContainer = document.getElementById(infoContainerId);
  commitInfoContainer.style.display = "block";
}
function hoverHide(nodeId) {
  commitNode = document.getElementById(nodeId);
  infoContainerId = "node-info-" + nodeId;
  commitInfoContainer = document.getElementById(infoContainerId);
  commitInfoContainer.style.display = "none";
}

function createLines(parentnodeId) {
  parentNode = document.getElementById(parentnodeId);
  parentNode_data = parentNode.getBoundingClientRect();
  parent_x = parentNode_data.x;
  parent_y = parentNode_data.y;
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
  children.forEach((childId) => {
    childNode = document.getElementById(childId);

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
  // document.getElementById("container").appendChild(svg)
}
function svgSizer() {
  var svg = document.getElementById("svg-canvas");
  var graph = document.getElementById("graph");
  g_height = graph.clientHeight;
  g_width = graph.clientWidth;
  svg.setAttribute("width", g_width);
  svg.setAttribute("height", g_height);
}
