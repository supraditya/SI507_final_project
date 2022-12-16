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