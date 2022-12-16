function hoverShow(nodeId)
{
    commitNode=document.getElementById(nodeId);
    infoContainerId="node-info-"+nodeId
    commitInfoContainer=document.getElementById(infoContainerId)
    commitInfoContainer.style.display="block";
}
function hoverHide(nodeId)
{
    commitNode=document.getElementById(nodeId);
    infoContainerId="node-info-"+nodeId
    commitInfoContainer=document.getElementById(infoContainerId)
    commitInfoContainer.style.display="none";
}

function createLines(parentnodeId)
{
    parentNode=document.getElementById(parentnodeId);
    parentNode_data=parentNode.getBoundingClientRect();
    parent_x=parentNode_data.x
    parent_y=parentNode_data.y
    str=parentNode.outerHTML
    str_start=str.search('name')
    str_end=str.lastIndexOf(' ')
    str_slice=str.substring(str_start, str_end)
    str_slice=str_slice.substring(8, str_slice.length-3)
    // Opening quote removal
    str_slice=str_slice.replace("'", "");
    // Closing quote removal
    str_slice=str_slice.replace("'", "");
    // Removing whitespaces
    str_slice=str_slice.replace(" ", "");
    children=str_slice.split(",")
    // console.log(children)
    // var svg = document.createElementNS("http://www.w3.org/2000/svg",'svg');
    // svg.setAttribute( "width",1000);
    // svg.setAttribute( "height",1000);
    // svg.setAttribute( "z-index",100);
    // svg.setAttribute( "position","absolute");
    // svg.setAttribute( "viewBox","0 0 1000 1000");
    var svg = document.getElementById('svg-canvas')
    children.forEach(childId => {
        childNode=document.getElementById(childId);
        childNode_data=childNode.getBoundingClientRect();
        child_x=childNode_data.x
        child_y=childNode_data.y

        var line=document.createElementNS("http://www.w3.org/2000/svg","line")
        line.setAttribute("x1", parent_x)
        line.setAttribute("y1", parent_y)
        line.setAttribute("x2", child_x)
        line.setAttribute("y2", child_y)
        line.setAttribute("stroke", "black")
        svg.appendChild(line)  
    });
    // document.getElementById("container").appendChild(svg)
}