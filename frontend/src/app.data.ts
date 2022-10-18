class DataModel{
    static currentTeam:Team
    static dreamTeam:Team

    public static async getTeam(teamName: string, year: string, isActive:boolean):Promise<Team>{
        DataModel.currentTeam =  await $.get(`/search?teamName=${teamName}&year=${year}&isActive=${isActive}`)
        return DataModel.currentTeam
    }

    public static async getStats(
        firstName: string,
        lastName: string
    ): Promise<Statistics> {
        return await $.get(`/stats?lastName=${lastName}&firstName=${firstName}`)
    }

    public static async getDreamTeam() :Promise<Team>{
        DataModel.dreamTeam = await $.get(`/dream`)
        return DataModel.dreamTeam
    }

    public static removeDreamTeam(personId: string) :void{
        $.ajax({
            url: `/dream?personId=${personId}`,
            type: 'DELETE',
            })
     
    }

    public static addDreamTeam(personId: string) :void{
        for(let player of DataModel.currentTeam.players){
            if(player.personId === personId){
                $.post(`/dream`,JSON.stringify(player))
            }
        }
        return
    }

}