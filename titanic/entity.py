class Entity:
    def __init__(self, context, fname, train, test, id, label):
        self._context = context # _는 default 접근 의미
        self._fname = fname
        self._train = train
        self._test = test
        self._id = id
        self._label = label

    # context get, set 을 만듭니다.

    @property
    def context(self) -> str:  # -> 는 리턴하는 타입을 의미
        return self._context

    @context
    def context(self, context):
        self._context = context

    
    # fname get, set 을 만듭니다.

    @property
    def fname(self) -> str:
        return self._fname

    @context
    def fname(self, fname):
        self._fname = fname


    # train get, set 을 만듭니다.


    # test get, set 을 만듭니다.


    # id get, set 을 만듭니다.


    # label get, set 을 만듭니다.
