var timer = function(){
    var timeLeft = timerLength;
    var preTime = leadTime;
    var $timer = $('.timer')

    var self = this;

    var normalize = function(n, digits){
        var s = n.toString();
        while(s.length < digits){
            s = '0' + s;
        }

        return s;
    };

    var timeToDisplay = function(t){
        var minutes = parseInt(t / 60);
        var seconds = t % 60;

        var toDisplay = normalize(minutes, 2) + ':' + normalize(seconds, 2);

        return toDisplay;
    };

    self.update = function(){
        var toDisplay = '';
        var run = true;
        if(preTime > 0) {
            toDisplay = '-' + timeToDisplay(preTime);
            preTime--;
        } else if(timeLeft <= 0) {
            $timer.addClass('expired');
            run = false;
            toDisplay = '00:00';
        } else {
            toDisplay = timeToDisplay(timeLeft);
            timeLeft--;
        }

        $timer.html(toDisplay);

        if(run){
            setTimeout(self.update, 1000);
        }
    };

    self.update();
};

Timer = timer();
