class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_cur_value_first_buy = [0]
        max_cur_profit_first_sell = [0]
        max_cur_value_second_buy = [0]
        max_cur_profit_second_sell = [0]
        for i in range(1,len(prices)):
            new_max_cur_value_first_buy = max(max_cur_value_first_buy[-1] + prices[i] - prices[i-1], 0)
            new_max_cur_profit_first_sell = max(max_cur_value_first_buy[-1] + prices[i] - prices[i-1], max_cur_profit_first_sell[-1])
            new_max_cur_value_second_buy = max(max_cur_value_second_buy[-1] + prices[i] - prices[i-1], max_cur_profit_first_sell[-1])
            new_max_cur_profit_second_sell = max(max_cur_value_second_buy[-1] + prices[i] - prices[i-1], max_cur_profit_second_sell[-1])
            max_cur_value_first_buy.append(new_max_cur_value_first_buy)
            max_cur_profit_first_sell.append(new_max_cur_profit_first_sell)
            max_cur_value_second_buy.append(new_max_cur_value_second_buy)
            max_cur_profit_second_sell.append(new_max_cur_profit_second_sell)
        return max_cur_profit_second_sell[-1]
