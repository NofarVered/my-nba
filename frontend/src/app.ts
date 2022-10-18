const DataModel = new DataModel()

const loadTeam = function (){
    const teamName: string = String($("#team-input").val())
    const year: string = String($("#year-input").val())
    const isActive: boolean = $('#active-player').is(':checked')
    const teamToRender: Team = await DataModel.getTeam(teamName, year, isActive)
    renderModel.RenderPlayerContainer(teamToRender)
}

const loadDreamTeam = async function(){
    const teamToRender: Team = await DataModel.getDreamTeam()
    renderModel.RenderPlayerContainer(teamToRender)
}

const loadStatistics = async function (personId: string ,firstName: string, lastName: string){
    const player: JQuery<HTMLElement> = $(`#${personId}`)
    if(player.children('.statistics').length > 0){
        player.find('.statistics').slideDown()
    }
    else{
        const statsToRender: Statistics = await DataModel.getStats(firstName, lastName)
        renderModel.renderStats(statsToRender, player)
    }
}

const addPlayer = async function (playerId: string): void{
    DataModel.addDreamTeam(playerId)
}

const removeDreamTeam = function (playerId: string): void{
    DataModel.removeDreamTeam(playerId)
    renderModel.loadDreamTeam()
}

