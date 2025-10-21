# API

## V1

Types:

```python
from inty.types.api import V1ListNotificationsResponse
```

Methods:

- <code title="get /api/v1/notifications/">client.api.v1.<a href="./src/inty/resources/api/v1/v1.py">list_notifications</a>(\*\*<a href="src/inty/types/api/v1_list_notifications_params.py">params</a>) -> <a href="./src/inty/types/api/v1_list_notifications_response.py">V1ListNotificationsResponse</a></code>
- <code title="post /api/v1/images">client.api.v1.<a href="./src/inty/resources/api/v1/v1.py">upload_image</a>(\*\*<a href="src/inty/types/api/v1_upload_image_params.py">params</a>) -> <a href="./src/inty/types/api/v1/api_response_dict.py">APIResponseDict</a></code>

### Auth

Types:

```python
from inty.types.api.v1 import AuthCreateGuestResponse
```

Methods:

- <code title="post /api/v1/auth/guest">client.api.v1.auth.<a href="./src/inty/resources/api/v1/auth/auth.py">create_guest</a>(\*\*<a href="src/inty/types/api/v1/auth_create_guest_params.py">params</a>) -> <a href="./src/inty/types/api/v1/auth_create_guest_response.py">AuthCreateGuestResponse</a></code>

#### Google

Types:

```python
from inty.types.api.v1.auth import GoogleLoginResponse
```

Methods:

- <code title="post /api/v1/auth/google/login">client.api.v1.auth.google.<a href="./src/inty/resources/api/v1/auth/google.py">login</a>(\*\*<a href="src/inty/types/api/v1/auth/google_login_params.py">params</a>) -> <a href="./src/inty/types/api/v1/auth/google_login_response.py">GoogleLoginResponse</a></code>

### Users

Types:

```python
from inty.types.api.v1 import UserDeleteAccountResponse
```

Methods:

- <code title="post /api/v1/users/delete-account">client.api.v1.users.<a href="./src/inty/resources/api/v1/users/users.py">delete_account</a>(\*\*<a href="src/inty/types/api/v1/user_delete_account_params.py">params</a>) -> <a href="./src/inty/types/api/v1/user_delete_account_response.py">UserDeleteAccountResponse</a></code>

#### Profile

Types:

```python
from inty.types.api.v1.users import Gender, User, ProfileUpdateResponse, ProfileMeResponse
```

Methods:

- <code title="put /api/v1/users/profile">client.api.v1.users.profile.<a href="./src/inty/resources/api/v1/users/profile.py">update</a>(\*\*<a href="src/inty/types/api/v1/users/profile_update_params.py">params</a>) -> <a href="./src/inty/types/api/v1/users/profile_update_response.py">ProfileUpdateResponse</a></code>
- <code title="get /api/v1/users/me">client.api.v1.users.profile.<a href="./src/inty/resources/api/v1/users/profile.py">me</a>() -> <a href="./src/inty/types/api/v1/users/profile_me_response.py">ProfileMeResponse</a></code>

#### Deletion

Types:

```python
from inty.types.api.v1.users import DeletionCheckEligibilityResponse
```

Methods:

- <code title="get /api/v1/users/deletion/check">client.api.v1.users.deletion.<a href="./src/inty/resources/api/v1/users/deletion.py">check_eligibility</a>() -> <a href="./src/inty/types/api/v1/users/deletion_check_eligibility_response.py">DeletionCheckEligibilityResponse</a></code>

### Report

Types:

```python
from inty.types.api.v1 import APIResponseDict, ReportCreateResponse
```

Methods:

- <code title="post /api/v1/report/">client.api.v1.report.<a href="./src/inty/resources/api/v1/report.py">create</a>(\*\*<a href="src/inty/types/api/v1/report_create_params.py">params</a>) -> <a href="./src/inty/types/api/v1/report_create_response.py">ReportCreateResponse</a></code>

### AI

#### Agents

Types:

```python
from inty.types.api.v1.ai import (
    Agent,
    AgentMetaData,
    AgentVisibility,
    APIResponseAgent,
    APIResponsePaginationDataAgent,
    ModelConfig,
    AgentCreateResponse,
    AgentListResponse,
)
```

Methods:

- <code title="post /api/v1/ai/agents">client.api.v1.ai.agents.<a href="./src/inty/resources/api/v1/ai/agents.py">create</a>(\*\*<a href="src/inty/types/api/v1/ai/agent_create_params.py">params</a>) -> <a href="./src/inty/types/api/v1/ai/agent_create_response.py">AgentCreateResponse</a></code>
- <code title="get /api/v1/ai/agents/{agent_id}">client.api.v1.ai.agents.<a href="./src/inty/resources/api/v1/ai/agents.py">retrieve</a>(agent_id) -> <a href="./src/inty/types/api/v1/ai/agent.py">Agent</a></code>
- <code title="put /api/v1/ai/agents/{agent_id}">client.api.v1.ai.agents.<a href="./src/inty/resources/api/v1/ai/agents.py">update</a>(agent_id, \*\*<a href="src/inty/types/api/v1/ai/agent_update_params.py">params</a>) -> <a href="./src/inty/types/api/v1/ai/agent.py">Agent</a></code>
- <code title="get /api/v1/ai/agents/me">client.api.v1.ai.agents.<a href="./src/inty/resources/api/v1/ai/agents.py">list</a>(\*\*<a href="src/inty/types/api/v1/ai/agent_list_params.py">params</a>) -> <a href="./src/inty/types/api/v1/ai/agent_list_response.py">AgentListResponse</a></code>
- <code title="delete /api/v1/ai/agents/{agent_id}">client.api.v1.ai.agents.<a href="./src/inty/resources/api/v1/ai/agents.py">delete</a>(agent_id) -> <a href="./src/inty/types/api/v1/ai/api_response_agent.py">APIResponseAgent</a></code>
- <code title="post /api/v1/ai/agents/{agent_id}/follow">client.api.v1.ai.agents.<a href="./src/inty/resources/api/v1/ai/agents.py">follow_agent</a>(agent_id) -> <a href="./src/inty/types/api/v1/api_response_dict.py">APIResponseDict</a></code>
- <code title="get /api/v1/ai/agents/following">client.api.v1.ai.agents.<a href="./src/inty/resources/api/v1/ai/agents.py">following</a>(\*\*<a href="src/inty/types/api/v1/ai/agent_following_params.py">params</a>) -> <a href="./src/inty/types/api/v1/ai/api_response_pagination_data_agent.py">APIResponsePaginationDataAgent</a></code>
- <code title="get /api/v1/ai/agents/recommend">client.api.v1.ai.agents.<a href="./src/inty/resources/api/v1/ai/agents.py">recommend</a>(\*\*<a href="src/inty/types/api/v1/ai/agent_recommend_params.py">params</a>) -> <a href="./src/inty/types/api/v1/ai/api_response_pagination_data_agent.py">APIResponsePaginationDataAgent</a></code>
- <code title="get /api/v1/ai/agents/search">client.api.v1.ai.agents.<a href="./src/inty/resources/api/v1/ai/agents.py">search</a>(\*\*<a href="src/inty/types/api/v1/ai/agent_search_params.py">params</a>) -> <a href="./src/inty/types/api/v1/ai/api_response_pagination_data_agent.py">APIResponsePaginationDataAgent</a></code>
- <code title="delete /api/v1/ai/agents/{agent_id}/follow">client.api.v1.ai.agents.<a href="./src/inty/resources/api/v1/ai/agents.py">unfollow_agent</a>(agent_id) -> <a href="./src/inty/types/api/v1/api_response_dict.py">APIResponseDict</a></code>

### Settings

Types:

```python
from inty.types.api.v1 import Settings
```

Methods:

- <code title="get /api/v1/settings/">client.api.v1.settings.<a href="./src/inty/resources/api/v1/settings.py">retrieve</a>() -> <a href="./src/inty/types/api/v1/settings.py">Settings</a></code>
- <code title="put /api/v1/settings/">client.api.v1.settings.<a href="./src/inty/resources/api/v1/settings.py">update</a>(\*\*<a href="src/inty/types/api/v1/setting_update_params.py">params</a>) -> <a href="./src/inty/types/api/v1/settings.py">Settings</a></code>

### Subscription

Types:

```python
from inty.types.api.v1 import (
    APIResponseSubscriptionStatus,
    APIResponseUsageStatistics,
    UserSubscription,
    SubscriptionListPlansResponse,
    SubscriptionVerifyResponse,
    SubscriptionWebhookResponse,
)
```

Methods:

- <code title="get /api/v1/subscription/status">client.api.v1.subscription.<a href="./src/inty/resources/api/v1/subscription/subscription.py">get_status</a>() -> <a href="./src/inty/types/api/v1/api_response_subscription_status.py">APIResponseSubscriptionStatus</a></code>
- <code title="get /api/v1/subscription/usage">client.api.v1.subscription.<a href="./src/inty/resources/api/v1/subscription/subscription.py">get_usage</a>() -> <a href="./src/inty/types/api/v1/api_response_usage_statistics.py">APIResponseUsageStatistics</a></code>
- <code title="get /api/v1/subscription/plans">client.api.v1.subscription.<a href="./src/inty/resources/api/v1/subscription/subscription.py">list_plans</a>() -> <a href="./src/inty/types/api/v1/subscription_list_plans_response.py">SubscriptionListPlansResponse</a></code>
- <code title="post /api/v1/subscription/verify">client.api.v1.subscription.<a href="./src/inty/resources/api/v1/subscription/subscription.py">verify</a>(\*\*<a href="src/inty/types/api/v1/subscription_verify_params.py">params</a>) -> <a href="./src/inty/types/api/v1/subscription_verify_response.py">SubscriptionVerifyResponse</a></code>
- <code title="post /api/v1/subscription/webhook">client.api.v1.subscription.<a href="./src/inty/resources/api/v1/subscription/subscription.py">webhook</a>() -> <a href="./src/inty/types/api/v1/subscription_webhook_response.py">SubscriptionWebhookResponse</a></code>

#### Admin

Types:

```python
from inty.types.api.v1.subscription import AdminProcessRefundResponse
```

Methods:

- <code title="post /api/v1/subscription/admin/refund">client.api.v1.subscription.admin.<a href="./src/inty/resources/api/v1/subscription/admin/admin.py">process_refund</a>(\*\*<a href="src/inty/types/api/v1/subscription/admin_process_refund_params.py">params</a>) -> <a href="./src/inty/types/api/v1/subscription/admin_process_refund_response.py">AdminProcessRefundResponse</a></code>

##### Plans

Types:

```python
from inty.types.api.v1.subscription.admin import (
    SubscriptionPlan,
    SubscriptionPlanType,
    PlanCreateResponse,
    PlanListResponse,
)
```

Methods:

- <code title="post /api/v1/subscription/admin/plans">client.api.v1.subscription.admin.plans.<a href="./src/inty/resources/api/v1/subscription/admin/plans.py">create</a>(\*\*<a href="src/inty/types/api/v1/subscription/admin/plan_create_params.py">params</a>) -> <a href="./src/inty/types/api/v1/subscription/admin/plan_create_response.py">PlanCreateResponse</a></code>
- <code title="get /api/v1/subscription/admin/plans">client.api.v1.subscription.admin.plans.<a href="./src/inty/resources/api/v1/subscription/admin/plans.py">list</a>(\*\*<a href="src/inty/types/api/v1/subscription/admin/plan_list_params.py">params</a>) -> <a href="./src/inty/types/api/v1/subscription/admin/plan_list_response.py">PlanListResponse</a></code>

##### Users

Methods:

- <code title="get /api/v1/subscription/admin/users/{user_id}/subscription">client.api.v1.subscription.admin.users.<a href="./src/inty/resources/api/v1/subscription/admin/users.py">get_subscription_status</a>(user_id) -> <a href="./src/inty/types/api/v1/api_response_subscription_status.py">APIResponseSubscriptionStatus</a></code>
- <code title="get /api/v1/subscription/admin/users/{user_id}/usage">client.api.v1.subscription.admin.users.<a href="./src/inty/resources/api/v1/subscription/admin/users.py">get_usage_statistics</a>(user_id) -> <a href="./src/inty/types/api/v1/api_response_usage_statistics.py">APIResponseUsageStatistics</a></code>

### Version

Types:

```python
from inty.types.api.v1 import VersionCheckResponse
```

Methods:

- <code title="post /api/v1/version/check">client.api.v1.version.<a href="./src/inty/resources/api/v1/version.py">check</a>() -> <a href="./src/inty/types/api/v1/version_check_response.py">VersionCheckResponse</a></code>

### Chats

Types:

```python
from inty.types.api.v1 import Chat, ChatListResponse
```

Methods:

- <code title="post /api/v1/chats/">client.api.v1.chats.<a href="./src/inty/resources/api/v1/chats/chats.py">create</a>(\*\*<a href="src/inty/types/api/v1/chat_create_params.py">params</a>) -> <a href="./src/inty/types/api/v1/chat.py">Chat</a></code>
- <code title="get /api/v1/chats/">client.api.v1.chats.<a href="./src/inty/resources/api/v1/chats/chats.py">list</a>(\*\*<a href="src/inty/types/api/v1/chat_list_params.py">params</a>) -> <a href="./src/inty/types/api/v1/chat_list_response.py">ChatListResponse</a></code>
- <code title="delete /api/v1/chats/{chat_id}">client.api.v1.chats.<a href="./src/inty/resources/api/v1/chats/chats.py">delete</a>(chat_id) -> <a href="./src/inty/types/api/v1/chat.py">Chat</a></code>
- <code title="post /api/v1/chat/completions/{agent_id}">client.api.v1.chats.<a href="./src/inty/resources/api/v1/chats/chats.py">create_completion</a>(agent_id, \*\*<a href="src/inty/types/api/v1/chat_create_completion_params.py">params</a>) -> <a href="./src/inty/types/api/v1/api_response_dict.py">APIResponseDict</a></code>
- <code title="get /api/v1/chats/voices/{voice_id}">client.api.v1.chats.<a href="./src/inty/resources/api/v1/chats/chats.py">retrieve_voice</a>(voice_id) -> object</code>

#### Agents

Types:

```python
from inty.types.api.v1.chats import ChatSettings, AgentUpdateSettingsResponse
```

Methods:

- <code title="post /api/v1/chats/agents/{agent_id}/messages/{message_id}/voice">client.api.v1.chats.agents.<a href="./src/inty/resources/api/v1/chats/agents.py">generate_message_voice</a>(message_id, \*, agent_id, \*\*<a href="src/inty/types/api/v1/chats/agent_generate_message_voice_params.py">params</a>) -> object</code>
- <code title="get /api/v1/chats/agents/{agent_id}/messages">client.api.v1.chats.agents.<a href="./src/inty/resources/api/v1/chats/agents.py">get_messages</a>(agent_id, \*\*<a href="src/inty/types/api/v1/chats/agent_get_messages_params.py">params</a>) -> object</code>
- <code title="get /api/v1/chats/agents/{agent_id}/settings">client.api.v1.chats.agents.<a href="./src/inty/resources/api/v1/chats/agents.py">get_settings</a>(agent_id) -> <a href="./src/inty/types/api/v1/chats/chat_settings.py">ChatSettings</a></code>
- <code title="put /api/v1/chats/agents/{agent_id}/settings">client.api.v1.chats.agents.<a href="./src/inty/resources/api/v1/chats/agents.py">update_settings</a>(agent_id, \*\*<a href="src/inty/types/api/v1/chats/agent_update_settings_params.py">params</a>) -> <a href="./src/inty/types/api/v1/chats/agent_update_settings_response.py">AgentUpdateSettingsResponse</a></code>

### TextToSpeech

Types:

```python
from inty.types.api.v1 import TextToSpeechListVoicesResponse
```

Methods:

- <code title="get /api/v1/text-to-speech/list-voices">client.api.v1.text_to_speech.<a href="./src/inty/resources/api/v1/text_to_speech.py">list_voices</a>(\*\*<a href="src/inty/types/api/v1/text_to_speech_list_voices_params.py">params</a>) -> <a href="./src/inty/types/api/v1/text_to_speech_list_voices_response.py">TextToSpeechListVoicesResponse</a></code>

# V2

## Chat

Types:

```python
from inty.types.v2 import ChatSendMessageResponse
```

Methods:

- <code title="post /api/v2/chat/completions/{agent_id}">client.v2.chat.<a href="./src/inty/resources/v2/chat.py">send_message</a>(agent_id, \*\*<a href="src/inty/types/v2/chat_send_message_params.py">params</a>) -> <a href="./src/inty/types/v2/chat_send_message_response.py">ChatSendMessageResponse</a></code>
