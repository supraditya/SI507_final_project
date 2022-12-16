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
    console.log(children)

}