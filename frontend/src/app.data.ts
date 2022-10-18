class Data{
    static currentTeam:Team
    static dreamTeam:Team

    public static async getTeam(teamName: string, year: string, isActive:boolean):Promise<Team>{
        Data.currentTeam =  await $.get(`/search?teamName=${teamName}&year=${year}&isActive=${isActive}`)
        return Data.currentTeam
    }

    public static async getStats(
        firstName: string,
        lastName: string
    ): Promise<Statistics> {
        return await $.get(`/stats?lastName=${lastName}&firstName=${firstName}`)
    }

    public static async getDreamTeam() :Promise<Team>{
        Data.dreamTeam = await $.get(`/dream`)
        return Data.dreamTeam
    }

    public static removeDreamTeam(personId: string) :void{
        $.ajax({
            url: `/dream?personId=${personId}`,
            type: 'DELETE',
            })
     
    }

    public static add_dream_team(personId: string) :void{
        for(let player of Data.currentTeam.players){
            if(player.personId === personId){
                $.post(`/dream`,JSON.stringify(player))
            }
        }
        return
    }

}