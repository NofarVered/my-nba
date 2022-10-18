import Handlebars from "handlebars";

class Render {
    public static RenderPlayerContainer(data:Team) {
        $(`#players-container`).empty();
        const userhtml = $(`#players-container`).html();
        const template = Handlebars.compile(userhtml);
        const newHTML = template({"player": data.players});
        $(`#players-container`).append(newHTML);

    }

    public static RenderPlayerStats(data:Statistics) {
        $(`#stats-container`).empty();
        const userhtml = $(`#stats-container`).html();
        const template = Handlebars.compile(userhtml);
        const newHTML = template({"player": data});
        $(`#stats-container`).append(newHTML);
    }

    public static EmptyPlayerStats() {
        $(`#stats-container`).empty();
    }
    
}
