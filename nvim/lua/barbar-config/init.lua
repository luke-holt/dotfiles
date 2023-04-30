require("barbar").setup {
    animations = false,
    closeable = true,
    clickable = true,
    icon_separator_left = '',
    autohide = true,

    -- insert buffer at end of line
    insert_at_end = true,
}

-- use nvim-tree keybinds to resize barbar by listening to nvim-tree events
local nvim_tree_events = require('nvim-tree.events')
local bufferline_api = require('bufferline.api')

local function get_tree_size()
  return require'nvim-tree.view'.View.width
end

nvim_tree_events.subscribe('TreeOpen', function()
  bufferline_api.set_offset(get_tree_size())
end)

nvim_tree_events.subscribe('Resize', function()
  bufferline_api.set_offset(get_tree_size())
end)

nvim_tree_events.subscribe('TreeClose', function()
  bufferline_api.set_offset(0)
end)
