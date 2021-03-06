# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from agent import BaseAgent
from backtest import Backtest, Generator
from model import BaseModel

import numpy as np
import pandas as pd

class Agent(BaseAgent):

    def __init__(self, name, *args, **kwargs):
        """
        Trading agent implementation.

        The backtest iterates over a set of sources and alerts the trading agent
        whenever a source is updated. These updates are conveyed through method
        calls to ...

        - on_quote(self, market_id, timestamp, book_state)
        - on_trade(self, market_id, timestamp, trade_state)
        - on_news(self, market_id, timestamp, news_state)
        - on_time(self, timestamp, timestamp_next)

        ..., all of which you are expected to implement yourself. In order to
        interact with a market, the trading agent may use the methods ...

        - submit_order(self, market_id, side, quantity, limit=None)
        - cancel_order(self, order)

        ... that create and delete orders waiting to be executed against the
        respective market's order book. Besides, this class implements a set
        of attributes ...

        - exposure (per market)
        - pnl_realized (per market)
        - pnl_unrealized (per market)
        - exposure_total
        - pnl_realized_total
        - pnl_unrealized_total
        - exposure_left
        - transaction_costs

        ... that may be used to monitor trading agent performance. The agent
        may also access attributes of related class instances, using the
        container attributes ...

        - orders -> [<Order>, *]
        - trades -> [<Trade>, *]
        - markets -> {<market_id>: <Market>, *}

        For more information, you may list all attributes and methods as well
        as access the docstrings available in the base class using
        `dir(BaseAgent)` and `help(BaseAgent.<method>)`, respectively.

        :param name:
            str, agent name
        """
        super(Agent, self).__init__(name, *args, **kwargs)

        # TODO: YOUR IMPLEMENTATION GOES HERE

        pass

    def on_quote(self, market_id:str, book_state:pd.Series):
        """
        This method is called after a new quote.

        :param market_id:
            str, market identifier
        :param book_state:
            pd.Series, including timestamp, bid/ask price/quantity for 10 levels
        """

        # TODO: YOUR IMPLEMENTATION GOES HERE

        pass

    def on_trade(self, market_id:str, trades_state:pd.Series):
        """
        This method is called after a new trade.

        :param market_id:
            str, market identifier
        :param trades_state:
            pd.Series, including timestamp, price, quantity
        """

        # TODO: YOUR IMPLEMENTATION GOES HERE

        pass

    def on_news(self, market_id:str, news_state:pd.Series):
        """
        This method is called after a news message.

        :param market_id:
            str, market identifier
        :param news_state:
            pd.Series, including timestamp, message
        """

        # TODO: YOUR IMPLEMENTATION GOES HERE

        pass

    def on_time(self, timestamp:pd.Timestamp, timestamp_next:pd.Timestamp):
        """
        This method is called with every iteration and provides the timestamps
        for both current and next iteration. The given interval may be used to
        submit orders before a specific point in time.

        :param timestamp:
            pd.Timestamp, timestamp recorded
        :param timestamp_next:
            pd.Timestamp, timestamp recorded in next iteration
        """

        # TODO: YOUR IMPLEMENTATION GOES HERE

        pass

class Model(BaseModel):

    def __init__(self, name, *args, **kwargs):
        """
        Neural network implementation.

        The model inherits from tf.keras.Model and implements a neural network
        architecture that can be used to make predictions based on book, trades
        and news data provided by the agent. In order to train and test the
        model on your data, you may use the methods ...

        - fit(self, ...)
        - evaluate(self, ...)

        ..., respectively. In order to make predictions on your data, you may
        use the method ...

        - predict(self, ...)

        ... that will either support or represent your trading decisions.

        For more information, please refer to the official tensorflow
        documentation at:

        https://www.tensorflow.org/api_docs/python/tf/keras/Model

        If you want to use supervised learning (classification, regression),
        you may use the default implementation for the above-mentioned methods.

        If you want to use reinforcement learning, however, you will need to
        override the above-mentioned methods with your custom logic that will
        for the most part replace your trading agent implementation.

        Note that you will have to take care of all necessary pre-processing
        steps yourself.

        For more information, you may list all attributes and methods as well
        as access the docstrings available in the base class using
        `dir(BaseModel)` and `help(BaseModel.<method>)`, respectively.

        :param name:
            str, model name
        """
        super(Model, self).__init__(name, *args, **kwargs)

        # TODO: YOUR IMPLEMENTATION GOES HERE

        pass

    def build(self, input_shape):
        """
        Set as instance attributes all layers to be used in call method.

        :param input_shape:
            tuple, input shape where first dimension is batch_size
        """

        # TODO: YOUR IMPLEMENTATION GOES HERE

        pass

    def call(self, x):
        """
        Implement a single forward pass using the defined layers.

        :param x:
            tf.Tensor, batch
        """

        # TODO: YOUR IMPLEMENTATION GOES HERE

        return x

if __name__ == "__main__":

    # TODO: SELECT SOURCES. You may delete or comment out the rest.

    sources = [
        # BASF
        "BAS.BOOK", "BAS.TRADES", "BAS.NEWS",
        # Bayer
        "BAY.BOOK", "BAY.TRADES", "BAY.NEWS",
        # BMW
        "BMW.BOOK", "BMW.TRADES", "BMW.NEWS",
        # Commerzbank
        "CBK.BOOK", "CBK.TRADES", "CBK.NEWS",
        # Daimler
        "DAI.BOOK", "DAI.TRADES", "DAI.NEWS",
        # Deutsche Bank
        "DBK.BOOK", "DBK.TRADES", "DBK.NEWS",
        # E.ON
        "EON.BOOK", "EON.TRADES", "EON.NEWS",
        # Fresenius Medical Care
        "FME.BOOK", "FME.TRADES", "FME.NEWS",
        # Fresenius
        "FRE.BOOK", "FRE.TRADES", "FRE.NEWS",
        # RWE
        "RWE.BOOK", "RWE.TRADES", "RWE.NEWS",
    ]

    # TODO: SELECT DATE RANGE. Please use format 'YYYY-MM-DD'.

    start_date = "2016-01-01"
    end_date = "2016-03-31"

    # TODO: INSTANTIATE YOUR TRADING AGENT. You may submit multiple agents.

    agent = Agent(
        name="test_agent",
    )

    # TODO: INSTANTIATE YOUR ML MODEL. Only if you need to make predictions.

    model = Model(
        name="test_model",
    )

    # insantiate generator
    generator = Generator(
        sources=sources,
        start_date=start_date,
        end_date=end_date,
    )
    # instantiate backtest
    backtest = Backtest(
        agent=agent,
        generator=generator,
    )
    # run backtest
    results = backtest.run()
