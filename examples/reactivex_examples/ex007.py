import reactivex

def lowercase():
    def _lowercase(source):
        def subscribe(observer, scheduler = None):
            def on_next(value):
                observer.on_next(value.lower())

            return source.subscribe(
                on_next,
                observer.on_error,
                observer.on_completed,
                scheduler=scheduler)
        return reactivex.create(subscribe)
    return _lowercase

reactivex.of("Alpha", "Beta", "Gamma", "Delta", "Epsilon").pipe(
        lowercase()
     ).subscribe(lambda value: print("Received {0}".format(value)))